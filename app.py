import os
import ast
import json
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv("MONGO_URI")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

######################
# Reusable functions #
######################

def recipe_init():
    # initialise blank recipe document to include all possible options including those not returned by create recipe form
    blank_recipe = {'title': '',
    'ingredients': [],
    'steps': [],
    'category': '',
    'owner': '',
    'pin': '',
    'dietary_info': {},
    'meal_info': {},
    'img_url': url_for('static', filename='img/stockimg.png') } 

    # add key value pairs for recipe filters and allow for additions/deletions to filter keywords at db level
    recipe_info = mongo.db.optionalTypes.find_one({'name': 'recipe_info'})
    for key in recipe_info['dietary']:
        blank_recipe['dietary_info'][key] = 'off'
    
    for key in recipe_info['meal']:
        blank_recipe['meal_info'][key] = 'off'

    return blank_recipe

def add_step(recipe, new_step_value):
    # creates a new list of recipe steps
    steps = recipe['steps']
    used_ids = []
    for item in steps:
        ids = item['step_id'].split('step_')
        used_ids.append(int(ids[1]))

    new_id = len(recipe['steps']) + 1
    for i in used_ids:
        if i == new_id:
            new_id += 1

    new_step = {'step_id': 'step_' + str(new_id), 'step': new_step_value}
    steps.append(new_step)
    return steps

def remove_ingredient(recipe, ingredient_to_remove):
    # creates a new list of ingredients by deleting the selected ingredient based on the button pressed
    # updates the database before reloading the page
    ingredient_list = recipe['ingredients']
    for index, ingredient in enumerate(ingredient_list):
        if ingredient['ingredient_id'] == ingredient_to_remove:
            del ingredient_list[index]    

    return ingredient_list

def add_ingredient(recipe, new_ingredient):
    # creates a new list of ingredients by appending a new ingredient to the list of ingredient objects from the db

    # finding the next available/unused ingredient id
    used_ids = []
    if len(recipe['ingredients']) > 0:
        for item in recipe['ingredients']:
            ids = item['ingredient_id'].split('ingredient_')
            used_ids.append(int(ids[1]))

        new_id = len(recipe['ingredients']) + 1
        for i in used_ids:
            if i == new_id:
                new_id += 1
    else :
        new_id = 1

    # adding the new ingredient
    new_ingredient_id = 'ingredient_' + str(new_id)
    new_ingredient['ingredient_id'] = new_ingredient_id
    if 'add_ingredient' in new_ingredient:
        del new_ingredient['add_ingredient']

    recipe['ingredients'].append(new_ingredient)
    return recipe['ingredients']



###################################
# Routes and associated functions #
###################################

@app.route('/')
@app.route('/home')
def home():
    # Route for returning to homepage and initialising the session cookie used to add recipes
    if not 'recipe' in session:
        session['recipe'] = recipe_init()
    return render_template('index.html')

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    # Route for displayng individual recipes
    recipe = mongo.db.scrambledeggs.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe)

@app.route('/browse_recipes')
def browse_recipes():
    # Renders the browse recipes page
    recipes = mongo.db.scrambledeggs.find()
    categories = mongo.db.optionalTypes.find_one({'name': 'recipe_type'})['values']
    recipe_info = mongo.db.optionalTypes.find_one({'name': 'recipe_info'})
    return render_template('browse_recipes.html', recipes = recipes, categories = categories, recipe_info=recipe_info)

@app.route('/filter_recipes', methods=['POST'])
def filter_recipes():
    # Returns recipes matching the selected filters
    if request.method == 'POST':
        form_values = request.form.to_dict()
        print(form_values)
        no_of_docs = mongo.db.scrambledeggs.count_documents(form_values)
        if no_of_docs > 0:
            recipes = mongo.db.scrambledeggs.find(form_values)
            categories = mongo.db.optionalTypes.find_one({'name': 'recipe_type'})['values']
            recipe_info = mongo.db.optionalTypes.find_one({'name': 'recipe_info'})       
            return render_template('browse_recipes.html', recipes=recipes, categories = categories, recipe_info=recipe_info)
    
    return redirect(url_for('home'))

@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    # returns recipes matching search terms a user might enter
    # matches are found from title, ingredient name, categories, dietary information and meal type
    recipes = mongo.db.scrambledeggs.find()
    if request.method == 'POST':
        search = request.form.to_dict()
        search_term = search['search_term'].lower()
        recipes_found = []
        for recipe in recipes:
            was_recipe_found = False
            if search_term in recipe['title'].lower():
                print('recipe found in title')
                recipes_found.append(recipe)
                continue
            elif search_term in recipe['category'].lower():
                print('recipe found in title')
                recipes_found.append(recipe)
                continue
            else :
                for ingredient in recipe['ingredients']:
                    if search_term in ingredient['ingredient_name'].lower():
                        print('recipe found in ingredients')
                        recipes_found.append(recipe)
                        was_recipe_found = True
                        break
                if not was_recipe_found:
                    for dietary_info in recipe['dietary_info']:
                        if search_term in dietary_info.lower() and recipe['dietary_info'][dietary_info] == 'on':
                            print('recipe found in dietary info')
                            recipes_found.append(recipe)
                            was_recipe_found = True
                            break
                    if not was_recipe_found:
                        for meal_info in recipe['meal_info']:
                            if search_term in meal_info.lower() and recipe['meal_info'][meal_info] == 'on':
                                print('recipe found in meal info')
                                recipes_found.append(recipe)
                                was_recipe_found = True
                                break

        categories = mongo.db.optionalTypes.find_one({'name': 'recipe_type'})['values']
        recipe_info = mongo.db.optionalTypes.find_one({'name': 'recipe_info'})                        
        return render_template(
            'browse_recipes.html', recipes=recipes_found, no_of_results=len(recipes_found), categories = categories, recipe_info=recipe_info)
    
    return redirect(url_for('home'))

@app.route('/create_recipe')
def create_recipe():
    # displays the create recipe page
    if not 'recipe' in session:
        session['recipe'] = recipe_init()

    measurements_list = mongo.db.optionalTypes.find_one({'name': 'measurements'})['values']
    categories = mongo.db.optionalTypes.find_one({'name': 'recipe_type'})['values']
    recipe_info = mongo.db.optionalTypes.find_one({'name': 'recipe_info'})
    recipe = session.get('recipe')

    return render_template('create_recipe.html', recipe=recipe, measurements=measurements_list, categories=categories, recipe_info=recipe_info)

@app.route('/add_recipe/', methods=['GET', 'POST'])
def add_recipe():
    # uses a session cookie to allow users to dynamically add ingredients and steps before saving the recipe to the database
    if request.method == 'POST':
        form_values = request.form.to_dict()
        
        session['recipe']['owner'] = form_values['owner'].lower()
        session['recipe']['pin'] = form_values['pin']
        session['recipe']['title'] = form_values['title']
        if form_values['img_url'] != '':
                session['recipe']['img_url'] = form_values['img_url']
        
        recipe = session.get('recipe')
        session.modified = True

        if 'remove_ingredient' in request.form:
            # removes an ingredient from the session cookie recipe object
            ingredient_to_remove = request.form['remove_ingredient']
            new_ingredients = remove_ingredient(recipe, ingredient_to_remove)
            session['recipe']['ingredients'] = new_ingredients
        elif 'add_ingredient' in request.form:
            # adds an ingredient to the session cookie recipe object
            new_ingredient = {'ingredient_name': form_values['ingredient_name'],
            'quantity': form_values['quantity'],
            'measurement': form_values['measurement']}
            new_ingredients = add_ingredient(recipe, new_ingredient) 
            session['recipe']['ingredients'] = new_ingredients
        elif 'add_step' in request.form:
            # adds a step to the session cookie recipe object
            new_step_value = form_values['new_step']
            session['recipe']['steps'] = add_step(session['recipe'], new_step_value)
        elif 'save_recipe' in request.form:
            session['recipe']['category'] = form_values['category']
            # remove unnecessary fields and values before further processing
            del form_values['ingredient_name'], form_values['quantity'], form_values['measurement']

            for form_key in form_values:
                # update dietary info
                for dict_key in recipe['dietary_info']:
                    if dict_key == form_key:
                        session['recipe']['dietary_info'][dict_key] = 'on'
                # update meal type
                for dict_key in recipe['meal_info']:
                    if dict_key == form_key:
                        session['recipe']['meal_info'][dict_key] = 'on'
            
            mongo.db.scrambledeggs.insert_one(session['recipe'])
            image = session['recipe']['img_url']
            session['recipe'] = recipe_init()
            
            return render_template('recipe_saved.html', title=form_values['title'], image=image)

    return redirect(url_for('create_recipe'))

@app.route('/edit_recipe')
def edit_recipe():
    # renders edit_recipe.html which asks for user's name and pin protection before proceeding
    return render_template('edit_recipe.html', doc_not_found=False)

@app.route('/find_recipe_to_edit', methods=['POST'])
def find_recipe_to_edit():
    # displays the recipes that match a user's name and pin code
    if request.method == 'POST':
        pincode = request.form.to_dict()
        owner = pincode['owner'].lower()
        recipes = mongo.db.scrambledeggs.find({'pin':pincode['pin'], 'owner': owner})
        no_of_docs = mongo.db.scrambledeggs.count_documents({'pin':pincode['pin'], 'owner': owner})
        
        if no_of_docs > 0:
            return render_template('choose_recipe_to_edit.html', recipes=recipes)
        else:
            return render_template('edit_recipe.html', doc_not_found=True)

    return redirect(url_for('home'))

@app.route('/recipe_to_update/<recipe_id>', methods=['GET', 'POST'])
def recipe_to_update(recipe_id):
    # takes the selected recipe and displays editing options
    recipe = mongo.db.scrambledeggs.find_one({'_id': ObjectId(recipe_id)})

    measurements_list = mongo.db.optionalTypes.find_one({'name': 'measurements'})['values']
    categories = mongo.db.optionalTypes.find_one({'name': 'recipe_type'})['values']

    return render_template('update_recipe.html', recipe=recipe, measurements=measurements_list, categories=categories)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    # updates the relevant recipe data in the database
    recipe = mongo.db.scrambledeggs.find_one({'_id': ObjectId(recipe_id)})
    
    if request.method == 'POST':
        form_values = request.form.to_dict()

        if 'remove_ingredient' in request.form:
            # removes an ingredient from the relevant recipe
            ingredient_to_remove = request.form['remove_ingredient']
            new_ingredients = remove_ingredient(recipe, ingredient_to_remove)
            mongo.db.scrambledeggs.update_one({'_id': ObjectId(recipe_id)}, {'$set' : {'ingredients': new_ingredients}})
        elif 'add_ingredient' in request.form:
            # adds an ingredient to the relevant recipe
            new_ingredient = {'ingredient_name': form_values['ingredient_name'],
            'quantity': form_values['quantity'],
            'measurement': form_values['measurement']}
            new_ingredients = add_ingredient(recipe, new_ingredient)
            mongo.db.scrambledeggs.update_one({'_id': ObjectId(recipe_id)}, {'$set' : {'ingredients': new_ingredients}})
        elif 'add_step' in request.form:
            # addsa step to the relevant recipe
            new_step_value = form_values['new_step']
            new_steps = add_step(recipe, new_step_value)
            mongo.db.scrambledeggs.update_one({'_id': ObjectId(recipe_id)}, {'$set' : {'steps': new_steps}})
        elif 'save_recipe' in request.form:
            recipe['title'] = form_values['title']
            recipe['category'] = form_values['category']
            # remove unnecessary fields and values before further processing
            del form_values['title'], form_values['category'] 
            del form_values['ingredient_name'], form_values['quantity'], form_values['measurement']

            # reset dietary info prior to overwrite with new selections
            for dict_key in recipe['dietary_info']:
                    recipe['dietary_info'][dict_key] = 'off'
            
            # reset meal type info prior to overwrite with new selections
            for dict_key in recipe['meal_info']:
                    recipe['meal_info'][dict_key] = 'off'

            for form_key in form_values:
                # update changes to ingredients 
                for index, ingredient in enumerate(recipe['ingredients']):
                    if ingredient['ingredient_id'] in form_key:
                        new_key = form_key.split('_' + ingredient['ingredient_id'])
                        ingredient[new_key[0]] = form_values[form_key]
                    recipe['ingredients'][index] = ingredient
                # update changes to steps
                for index, step in enumerate(recipe['steps']):
                    if step['step_id'] == form_key:
                        step['step'] = form_values[form_key]
                        if step['step'] == '':
                            del recipe['steps'][index]
                        else: 
                            recipe['steps'][index] = step

                # update dietary info
                for dict_key in recipe['dietary_info']:
                    if dict_key == form_key:
                        recipe['dietary_info'][dict_key] = 'on'
                # update meal type
                for dict_key in recipe['meal_info']:
                    if dict_key == form_key:
                        recipe['meal_info'][dict_key] = 'on'

            
            recipe['img_url'] = form_values['img_url']

            mongo.db.scrambledeggs.replace_one({'_id': ObjectId(recipe_id)}, recipe)

            recipes = mongo.db.scrambledeggs.find({'pin':recipe['pin'], 'owner': recipe['owner']})
            return render_template('choose_recipe_to_edit.html', recipes=recipes)
    
    # reloads the current recipe for further editing if the save recipe button has not yet been clicked
    return redirect(url_for('recipe_to_update', recipe_id=recipe_id))

@app.route('/remove_recipe')
def remove_recipe():
    # renders remove_recipe.html which asks for user's name and pin protection before proceeding
    return render_template('remove_recipe.html', doc_not_found=False)

@app.route('/find_recipes_for_removal', methods=['POST'])
def find_recipes_for_removal():
    # displays the recipes that match a user's name and pin code
    if request.method == 'POST':
        pincode = request.form.to_dict()
        owner = pincode['owner'].lower()
        recipes = mongo.db.scrambledeggs.find({'pin':pincode['pin'], 'owner': owner})
        no_of_docs = mongo.db.scrambledeggs.count_documents({'pin':pincode['pin'], 'owner': owner})
        
        if no_of_docs > 0:
            return render_template('choose_recipe_to_remove.html', recipes=recipes)
        else:
            return render_template('remove_recipe.html', doc_not_found=True)

    return redirect(url_for('home'))

@app.route('/delete_recipe/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    # remove the relevant recipe from the db

    if request.method == 'POST':
        # check if there is still a document with the relevant _id
        # If the user clicks the browsers back button they will see the deleted documents due to the 
        # previous page being stored in the browser cache. In this case, this check prevents the app
        # from crashing if the user tries to delete an already deleted document by changing the message
        # parameter passed to recipe_removed.html
        if mongo.db.scrambledeggs.count_documents({"_id": ObjectId(recipe_id)}) > 0:
            recipe = mongo.db.scrambledeggs.find_one({"_id": ObjectId(recipe_id)})
            title = recipe['title']
            removed_message = f'Your recipe \"{title}\" has been deleted'
            mongo.db.scrambledeggs.remove({"_id": ObjectId(recipe_id)}, {True})
            return render_template('recipe_removed.html', message=removed_message)
        else :
            removed_message = "That recipe has already been deleted"
            return render_template('recipe_removed.html', message=removed_message)


if __name__ =='__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)
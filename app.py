import os
import ast
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "TossedSalad"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

# Reusable functions
def recipe_init():
    # initialise blank recipe document to include all possible options including those not returned by create recipe form
    blank_recipe = {'title': '',
    'ingredients': [],
    'steps': [],
    'category': '',
    'owner': '',
    'pin': '',
    'dietary_info': {},
    'meal_info': {} } 

    # add key value pairs for recipe filters and allow for additions/deletions to filter keywords at db level
    recipe_info = mongo.db.optionalTypes.find_one({'name': 'recipe_info'})
    for key in recipe_info['dietary']:
        blank_recipe['dietary_info'][key] = 'off'
    
    for key in recipe_info['meal']:
        blank_recipe['meal_info'][key] = 'off'

    return blank_recipe

@app.route('/')
@app.route('/home')
def home():
    # Route for returning to homepage
    return render_template('index.html')

@app.route('/browse_recipes')
def browse_recipes():
    # Browse and find recipes for viewing
    recipes = mongo.db.scrambledeggs.find()
    return render_template('recipe.html', recipes = recipes)

@app.route('/create_recipe')
def create_recipe():
    # displays the create recipe page
    measurements_list = mongo.db.optionalTypes.find_one({'name': 'measurements'})['values']
    categories = mongo.db.optionalTypes.find_one({'name': 'recipe_type'})['values']
    recipe_info = mongo.db.optionalTypes.find_one({'name': 'recipe_info'})

    return render_template('create_recipe.html', measurements=measurements_list, categories=categories, recipe_info=recipe_info)

@app.route('/add_recipe/', methods=['POST'])
def add_recipe():
    # Adding a new recipe document to database
    
    # initialise recipe document
    recipe_to_add = recipe_init()

    if request.method == 'POST':
        recipe_holder = request.form.to_dict()

        # processing steps info from <textarea> into an array so each step 
        # can be treated separately upon retrieval from mongodb
        steps_holder = recipe_holder['steps']

        # There is a need to replace any instances of double quotes to avoid errors when converting 
        # string to dict object using json.loads()
        # First replace any double quotes with single quotes
        steps_holder = steps_holder.replace('"', "'")
        # then replace <p> with double quotes, 
        # <p> simply used in place of double quotes in form data to avoid being replaced in first replace operation
        steps_holder = steps_holder.replace('<p>', '"')

        steps = steps_holder.split('<br>')
        if len(steps) >= 1 :
            steps.pop()
            for i, val in enumerate(steps):
                steps[i] = json.loads(val)
                
        recipe_holder['steps'] = steps
        # processing ingredients/quantity/measurement info from <textarea> 
        # into an array so each step can be treated separately upon retrieval from mongodb
        ingredients_holder = recipe_holder['ingredients']
        ingredients = ingredients_holder.split('<br>')
        if len(ingredients) >= 1:
            ingredients.pop()
            for i, val in enumerate(ingredients):
                ingredients[i] = ast.literal_eval(val)            
        recipe_holder['ingredients'] = ingredients

        recipe_holder['owner'] = recipe_holder['owner'].lower()
        # replace values in blank document with form data

        for i in recipe_holder:
            add_to_recipe = True
            for key in recipe_to_add['dietary_info']:
                if key == i:
                    recipe_to_add['dietary_info'][key] = 'on'
                    add_to_recipe = False

            for key in recipe_to_add['meal_info']:
                if key == i:
                    recipe_to_add['meal_info'][key] = 'on'
                    add_to_recipe = False

            if add_to_recipe:
                recipe_to_add[i] = recipe_holder[i]

        # insert new recipe document in db
        recipe_db_connection = mongo.db.scrambledeggs
        recipe_db_connection.insert_one(recipe_to_add)

    return redirect(url_for('create_recipe'))

@app.route('/edit_recipe')
def edit_recipe():
    return render_template('edit_recipe.html', doc_not_found=False)

@app.route('/find_recipe_to_edit', methods=['POST'])
def find_recipe_to_edit():
    # displays the recipes that m
    if request.method == 'POST':
        pincode = request.form.to_dict()
        owner = pincode['owner'].lower()
        recipes = mongo.db.scrambledeggs.find({'pin':pincode['pin'], 'owner': owner})
        no_of_docs = mongo.db.scrambledeggs.count_documents({'pin':pincode['pin']})
        
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
    recipe = mongo.db.scrambledeggs.find_one({'_id': ObjectId(recipe_id)})
    
    if request.method == 'POST':
        form_values = request.form.to_dict()
        if 'remove_ingredient' in request.form:
            ingredient_to_remove = request.form['remove_ingredient']
            new_ingredients = remove_ingredient(recipe, ingredient_to_remove)
            mongo.db.scrambledeggs.update_one({'_id': ObjectId(recipe_id)}, {'$set' : {'ingredients': new_ingredients}})
        elif 'add_ingredient' in request.form:
            new_ingredient = {'ingredient_name': form_values['ingredient_name'],
            'quantity': form_values['quantity'],
            'measurement': form_values['measurement']}
            new_ingredients = add_ingredient(recipe, new_ingredient)
            mongo.db.scrambledeggs.update_one({'_id': ObjectId(recipe_id)}, {'$set' : {'ingredients': new_ingredients}})
        elif 'add_step' in request.form:
            new_step_value = form_values['new_step']
            new_steps = add_step(recipe, new_step_value)
            mongo.db.scrambledeggs.update_one({'_id': ObjectId(recipe_id)}, {'$set' : {'steps': new_steps}})
        elif 'save_recipe' in request.form:
            recipe['title'] = form_values['title']
            recipe['category'] = form_values['category']
            # remove unnecessary fields and values before further processing
            del form_values['title'], form_values['category'] 
            del form_values['ingredient_name'], form_values['quantity'], form_values['measurement']

            # reset dietary info prior to overwrite
            for dict_key in recipe['dietary_info']:
                    recipe['dietary_info'][dict_key] = 'off'
            
            # reset meal type info prior to overwrite
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

            mongo.db.scrambledeggs.replace_one({'_id': ObjectId(recipe_id)}, recipe)
    
    return redirect(url_for('recipe_to_update', recipe_id=recipe_id))

def add_step(recipe, new_step_value):
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
    # and updates the database before reloading the page

    # finding the next available/unused ingredient id
    used_ids = []
    for item in recipe['ingredients']:
        ids = item['ingredient_id'].split('ingredient_')
        used_ids.append(int(ids[1]))

    new_id = len(recipe['ingredients']) + 1
    for i in used_ids:
        if i == new_id:
            new_id += 1

    # adding the new ingredient
    new_ingredient_id = 'ingredient_' + str(new_id)
    new_ingredient['ingredient_id'] = new_ingredient_id
    if 'add_ingredient' in new_ingredient:
        del new_ingredient['add_ingredient']

    recipe['ingredients'].append(new_ingredient)
    return recipe['ingredients']

if __name__ =='__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)
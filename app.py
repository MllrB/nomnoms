import os
import ast
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

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/browse_recipes')
def browse_recipes():
    recipes = mongo.db.scrambledeggs.find()
    return render_template('recipe.html', recipes = recipes)

@app.route('/create_recipe')
def create_recipe():
    measurements_list = mongo.db.optionalTypes.find_one({'name': 'measurements'})['values']
    categories = mongo.db.optionalTypes.find_one({'name': 'recipe_type'})['values']
    extra_info = mongo.db.optionalTypes.find_one({'name': 'recipe_info'})['values']

    return render_template('create_recipe.html', measurements=measurements_list, categories=categories, recipe_info=extra_info)

@app.route('/add_recipe/', methods=['POST'])
def add_recipe():
    # Adding a new recipe document to database
    new_recipe = mongo.db.scrambledeggs
    if request.method == 'POST':
        recipe_holder = request.form.to_dict()
        # processing steps info from <textarea> into an array so each step 
        # can be treated separately upon retrieval from mongodb
        steps_holder = recipe_holder['steps']
        steps = steps_holder.split('<br>')
        if len(steps) >= 1 :
            steps.pop()
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

        new_recipe.insert_one(recipe_holder)

    return redirect(url_for('create_recipe'))


if __name__ =='__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)
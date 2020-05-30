import os
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

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    new_recipe = mongo.db.scrambledeggs
    if request.method == 'POST':
        new_recipe.insert_one(request.form.to_dict())
    return redirect(url_for('create_recipe'))


if __name__ =='__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)
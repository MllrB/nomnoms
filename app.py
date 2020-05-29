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

list_of_measurements = ['qty', 'grams', 'kilos', 'ml', 'oz', 'lb', 'cups', 'tbsp', 'tsp']

@app.route('/')
@app.route('/create_recipe/<measurement>')
def create_recipe():
    return render_template('create_recipe.html', measurement=list_of_measurements)

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    new_recipe = mongo.db.scrambledeggs
    if request.method == 'POST':
        new_recipe.insert_one(request.form.to_dict())
    return redirect(url_for('create_recipe'))


if __name__ =='__main__':
    app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)
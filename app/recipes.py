# this is the "app/recipes.py" file...

# IMPORTS

import json
from pprint import pprint
from IPython.display import Image, display

# packages (require installation)
import requests

# ENV VARS

import os
from dotenv import load_dotenv

load_dotenv() # look in the .env file for env variables

SPOONACULAR = os.getenv("SPOONACULAR", default="demo")

# RECIPE REPORT


# Create Criteria to Piece Together URL



def get_recipes(cuisine_type, diet_type, meal_type, intolerances):
    original_url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR}&cuisine={cuisine_type}&diet={diet_type}&intolerances={intolerances}&type={meal_type}&number=10&addRecipeInstructions=True&instructionsRequired=True"


    response = requests.get(original_url)

    recipes_orig = json.loads(response.text)

    id_values = []
    for recipe in recipes_orig["results"]:
        id_values.append(recipe["id"])
        
    id = str(id_values)[1:-1]

    recipe_url = f"https://api.spoonacular.com/recipes/informationBulk?apiKey={SPOONACULAR}&ids={id}"
    recipe_response = requests.get(recipe_url)

    recipes = json.loads(recipe_response.text)

    return recipes
         


# the weird main conditional says
# only run the indented code if you are running this file
# from the command line
# otherwise if importing from this file, ignore the stuff below

if __name__ == "__main__":

    # only if running from command line will this get reached

    cuisine = input("Please select a cuisine (e.g. 'Greek'):")
    diet = input("Please select a specific diet (e.g. 'Vegan'):")
    meal = input("Please select a meal type (e.g. 'Appetizer'):")
    intolerance = input("Please select an intolerance (e.g. 'Soy'):")

    recipes = get_recipes(cuisine, diet, meal, intolerance)

    for info in recipes:
        print('-------')
        display(Image(url=info['image'],height=100))
        print(info["title"])
        print(info["spoonacularSourceUrl"])

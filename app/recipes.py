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
    recipe_url = f"https://api.spoonacular.com/food/search?apiKey={SPOONACULAR}&query={cuisine_type}&{diet_type}&{intolerances}&{meal_type}&number=10&addRecipeNutrition=True&addRecipeInstructions=True"
    response = requests.get(recipe_url)
    # print(recipe_url)
    recipes = json.loads(response.text)


    results = []

    for recipe in recipes["searchResults"]:
        results.append(recipe["results"])

    # print(results)

    return results[0]
         


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

    for recipe in recipes:
        print('-------')
        display(Image(url=recipe['image'],height=100))
        print(recipe["name"])
        print(recipe["link"])

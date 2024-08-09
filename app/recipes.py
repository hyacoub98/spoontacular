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


    for result in results[0]:
        print('-------')
        display(Image(url=result['image'],height=100))
        print(result["name"])
        print(result["link"])

    return
         

cuisine = input("Please select a cuisine (e.g. 'Middle Eastern'):")
diet = input("Please select a specific diet (e.g. 'Vegan'):")
meal = input("Please select a meal type (e.g. 'Appetizer'):")
intolerance = input("Please select an intolerance (e.g. 'Soy'):")

get_recipes(cuisine, diet, meal, intolerance)


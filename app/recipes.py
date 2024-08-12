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

    first_recipe = [recipes[0]["image"],recipes[0]["name"],recipes[0]["link"]]
    second_recipe = [recipes[1]["image"],recipes[1]["name"],recipes[1]["link"]]
    third_recipe = [recipes[2]["image"],recipes[2]["name"],recipes[2]["link"]]
    fourth_recipe = [recipes[3]["image"],recipes[3]["name"],recipes[3]["link"]]
    fifth_recipe = [recipes[4]["image"],recipes[4]["name"],recipes[4]["link"]]
    sixth_recipe = [recipes[5]["image"],recipes[5]["name"],recipes[5]["link"]]
    seventh_recipe = [recipes[6]["image"],recipes[6]["name"],recipes[6]["link"]]
    eighth_recipe = [recipes[7]["image"],recipes[7]["name"],recipes[7]["link"]]
    nineth_recipe = [recipes[8]["image"],recipes[8]["name"],recipes[8]["link"]]
    tenth_recipe = [recipes[9]["image"],recipes[9]["name"],recipes[9]["link"]]

    print(first_recipe)
    print(second_recipe)
    print(third_recipe)
    print(fourth_recipe)
    print(fifth_recipe)
    print(sixth_recipe)
    print(seventh_recipe)
    print(eighth_recipe)
    print(nineth_recipe)
    print(tenth_recipe)


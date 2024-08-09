# this is the "app/recipes.py" file...

# IMPORTS

import json
from pprint import pprint
from statistics import mean

# packages (require installation)
import requests

# ENV VARS

import os
from dotenv import load_dotenv

load_dotenv() # look in the .env file for env variables

API_KEY = os.getenv("SPOONACULAR", default="demo")

# RECIPE REPORT

recipe_url = f"https://api.spoonacular.com/recipes/716429/information?apiKey={SPOONACULAR}"

response = requests.get(recipe_url)

recipes = json.loads(response.text)
# print(type(recipes))
# pprint(recipes)
# print(recipes.keys())


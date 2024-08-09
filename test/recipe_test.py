# this is the "test/recipe_test.py" file...
# IMPORTS
from app.recipes import get_recipes

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


def test_recipes():
    data = get_recipes("Greek", "Vegan", "appetizer", "soy")
    assert isinstance(results, list) 
    assert len(results[0]) == 10




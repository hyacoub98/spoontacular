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


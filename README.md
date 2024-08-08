# spoontacular
Python Programming Final Project

We are hoping to leverage the Spoonacular API that will allow users to search for different recipes by filtering for what they'd like.

An example could be if they search for a recipe by calorie amount, protein, dietary restrictions, etc.

We would like the user to be presented with a variety of options - if they want to select from a type of cuisine, be presented with the cuisine types and then select one.

After they find a recipe they would like to try, we would like to give them the option to email the recipe to themselves as a way to save it.

# Data Dictionary:

This link provides more information on the definition of the variables within each site.
https://spoonacular.com/food-api/docs#Search-Recipes-Complex






## Setup

Create virtual environment:

```sh
conda create -n spoon-env python=3.11
```

Activate the environment:

```sh
conda activate spoon-env
```

Install packages:

```sh
#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
```


Obtain an [API Key](https://spoonacular.com/food-api) from Spoonacular. Then create a ".env" file in the root directory of the repo, and paste some contents in like this, but using your own api key:

```sh
# this is the ".env" file:

SPOONACULAR="__________"
```

## Usage

Run the script:

Recipe criteria:

```sh
python -m app.recipes
```



Run the web app (then view in the browser at ):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```


## Testing

Run tests:

```sh
pytest
```



# this is the "web_app/routes/recipe_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.recipes import get_recipes

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipes/home")
def recipe_home():
    print("WELCOME, PLEASE SELECT YOUR RECIPE CRITERIA...")
    recipe_home = get_recipes()
    return render_template("recipe_home.html", recipe_home=recipe_home)

@recipe_routes.route("/recipes/cards", methods=["GET", "POST"])
def recipes():
    print("HERE ARE THE RECIPES FROM YOUR SEARCH...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)

    print("REQUEST DATA:", request_data)

    cuisine_type = request_data.get("cuisine_type") or "Greek" # get specified value or use default
    diet_type = request_data.get("diet_type") or "Vegan" # get specified value or use default
    meal_type = request_data.get("meal_type") or "Appetizer" # get specified value or use default
    intolerances = request_data.get("intolerances") or "Soy" # get specified value or use default

    try:
        recipes = get_recipes(cuisine_type=cuisine_type,diet_type=diet_type,meal_type=meal_type,intolerances=intolerances)
        

        flash("Fetched Real-time Recipe Data!", "success")
        return render_template("recipe_cards.html",
            recipes=recipes,
            cuisine_type=cuisine_type,
            diet_type=diet_type,
            meal_type=meal_type,
            intolerances=intolerances
        )
    
    except Exception as err:
        print('OOPS', err)

        return redirect("/recipes/home")




@recipe_routes.route("/api/recipes.json")
def recipes_api():
    print("LIST RECIPES (API)...")
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    cuisine_type = request_data.get("cuisine_type") or "Greek" # get specified value or use default
    diet_type = request_data.get("diet_type") or "Vegan" # get specified value or use default
    meal_type = request_data.get("meal_type") or "Appetizer" # get specified value or use default
    intolerances = request_data.get("intolerances") or "Soy" # get specified value or use default

    try:
        recipes = get_recipes(cuisine_type=cuisine_type,diet_type=diet_type,meal_type=meal_type,intolerances=intolerances)


        flash("Fetched Real-time Recipe Data!", "success")
        return {"recipes": recipes, "cuisine_type": cuisine_type, "diet_type": diet_type, "meal_type": meal_type, "intolerances": intolerances}
    except Exception as err:
        print('OOPS', err)
        return {"message":"Recipe Data Error. Please try again."}, 404

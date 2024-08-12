
# this is the "web_app/routes/recipe_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.recipes import get_recipes

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipes/home")
def recipe_home():
    print("WELCOME, PLEASE SELECT YOUR RECIPE CRITERIA...")
    # recipes = get_recipes()
    return render_template("recipe_home.html")
    # , recipes=recipes)

@recipe_routes.route("/recipes/card", methods=["GET", "POST"])
def recipes():
    print("HERE ARE THE RECIPES FROM YOUR SEARCH...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)

    print("REQUEST DATA:", request_data)

    cuisine = request_data.get("cuisine_type") or "Greek" # get specified value or use default
    diet = request_data.get("diet_type") or "Vegan" # get specified value or use default
    meal = request_data.get("meal_type") or "Appetizer" # get specified value or use default
    intolerance = request_data.get("intolerances") or "Soy" # get specified value or use default

    try:
        recipes = get_recipes(cuisine_type=cuisine,diet_type=diet,meal_type=meal,intolerances=intolerance)
        
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

        flash("Fetched Real-time Recipe Data!", "success")
        return render_template("recipe_cards.html",
            cuisine_type=cuisine,
            diet_type=diet,
            meal_type=meal,
            intolerances=intolerance
        )
    
    except Exception as err:
        print('OOPS', err)

        return redirect("/recipes/home")




@recipe_routes.route("/api/recipes.json")
def recipes_api():
    print("LIST RECIPES (API)...")
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    cuisine = url_params.get("cuisine_type") or "Greek"
    diet = url_params.get("diet_type") or "Vegan"
    meal = url_params.get("meal_type") or "Appetizer"
    intolerance = url_params.get("intolerances") or "Soy"

    try:
        recipes = get_recipes(cuisine_type=cuisine,diet_type=diet,meal_type=meal,intolerances=intolerance)
        
        for result in recipes:
            display(Image(url=result['image'],height=100))
            print(result["name"])
            print(result["link"])

        flash("Fetched Real-time Recipe Data!", "success")
        return {"cuisine_type": cuisine, "diet_type": diet, "meal_type": meal, "intolerances": intolerance}
    except Exception as err:
        print('OOPS', err)
        return {"message":"Market Data Error. Please try again."}, 404

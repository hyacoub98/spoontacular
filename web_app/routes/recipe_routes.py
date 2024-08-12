
# this is the "web_app/routes/recipe_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.recipes import get_recipes

recipe_routes = Blueprint("recipe_routes", __name__)

@recipe_routes.route("/recipes/home")
def recipes():
    print("WELCOME, PLEASE SELECT YOUR RECIPE CRITERIA...")
    recipes = get_recipes()
    return render_template("recipe_home.html", recipes=recipes)

@recipe_routes.route("/recipes/card", methods=["GET", "POST"])
def recipe_cards():
    print("HERE ARE THE RECIPES FROM YOUR SEARCH...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)

    print("REQUEST DATA:", request_data)

    cuisine = request_data.get("cuisine_type") or "Greek" # get specified symbol or use default
    diet = request_data.get("diet_type") or "Vegan" # get specified symbol or use default
    meal = request_data.get("meal_type") or "Appetizer" # get specified symbol or use default
    intolerance = request_data.get("intolerances") or "Soy" # get specified symbol or use default

    try:
        results_var = get_recipes(cuisine_type=cuisine,diet_type=diet,meal_type=meal,intolerances=intolerance)
        
        for result in results_var:
            display(Image(url=result['image'],height=100))
            print(result["name"])
            print(result["link"])

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
    recipes = get_recipes()
    return {"recipes": recipes}
    
# this is the "test/recipe_test.py" file...
# IMPORTS
from app.recipes import get_recipes



def test_recipes():
    data = get_recipes("Greek", "Vegan", "appetizer", "soy")
    assert isinstance(data, list) 
    assert len(data) == 10




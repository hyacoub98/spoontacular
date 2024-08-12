# this is the "web_app/__init__.py" file...

import os
from flask import Flask

from web_app.routes.recipe_routes import recipe_routes

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!



def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    
    app.register_blueprint(recipe_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)


from flask import Blueprint, Flask
main = Blueprint('main',__name__)
from flask_bootstrap import Bootstrap
from config import configOptions
from . import views,error


bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(configOptions[config_name])

   # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
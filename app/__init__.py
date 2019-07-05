# Import extensions
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

# Create extension instances
app = Flask(__name__)
db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    """
    Function that handles all extensions and blueprints

    Args:
        ConfigName:
    """

    # Setting up app configurations
    app.config.from_object(config_options[config_name])
    
    # Initialize flask extensions
    db.init_app(app)
    bootstrap.init_app(app)
    

    # Import app blueprints
    from .main import main as main_blueprint
    
    # Register app blueprints
    app.register_blueprint(main_blueprint)



    return app


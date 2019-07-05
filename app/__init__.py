# Import extensions
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# Create extension instances
app = Flask(__name__)
# db = SQLAlchemy()

def create_app(config_name):
    """
    Function that handles all extensions and blueprints

    Args:
        ConfigName:
    """
    
    # Initialize flask extensions
    # db.init_app(app)
    

    # Import app blueprints
    from .main import main as main_blueprint
    
    # Register app blueprints
    app.register_blueprint(main_blueprint)



    return app


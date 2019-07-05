# Import extensions
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import config_options

# Create extension instances
app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



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
    from .auth import auth as auth_blueprint
    # Register app blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)



    return app


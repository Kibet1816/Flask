import os

class Config:
    SECRET_KEY = 'gorgonsonofskrygon'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):

    DEBUG = True

config_options = {
    'production': ProdConfig,
    'development':DevConfig,
    'tests': TestConfig
}
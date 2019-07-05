import os

class Config:
    SECRET_KEY = 'gorgonsonofskrygon'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://denis1816:kibet@localhost/blogging'
    

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):

    DEBUG = True

config_options = {
    'production': ProdConfig,
    'development':DevConfig,
    'tests': TestConfig
}
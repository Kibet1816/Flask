import os

class Config():
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://denis1816:kibet@localhost/pomodoro'
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    pass

class TestConfig(Config):
    pass

config_options = {
    'production': ProdConfig,
    'development':DevConfig,
    'tests': TestConfig
}
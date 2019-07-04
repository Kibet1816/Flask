class Config():
    pass

class ProdConfig(Config):
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
import secrets

class Config:
    """Base class for Flask Config
    """
    PORT = 5000 #port to host server on

class DevConfig(Config):
    """Config for dev
    """
    SECRET_KEY = secrets.token_hex(nbytes=32)
    DEBUG = True

class ProductionConfig(Config):
    """Config for dev
    """
    SECRET_KEY = secrets.token_hex(nbytes=32)
    DEBUG = False
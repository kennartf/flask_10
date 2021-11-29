import os

class Config(object):
    SECRET_KEY=os.urandom(24).hex()
    # SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(base_dir,'app.db')
    SQLALCHEMY_DATABASE_URI='sqlite:///password:p4ssw0rd:localhost'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
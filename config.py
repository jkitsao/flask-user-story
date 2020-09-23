import os




class Config:
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://osjdxommkpajya:331568f21e2091dbffde86f61ff2c8d8598cf8d44482174f7d4d2fcc29c5e143@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d4ji8t73b1mtp5'

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    
class ProdConfig(Config):
   

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   
class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://osjdxommkpajya:331568f21e2091dbffde86f61ff2c8d8598cf8d44482174f7d4d2fcc29c5e143@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d4ji8t73b1mtp5'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://osjdxommkpajya:331568f21e2091dbffde86f61ff2c8d8598cf8d44482174f7d4d2fcc29c5e143@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d4ji8t73b1mtp5'
    
    
    DEBUG = True
    ENV = 'production'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}


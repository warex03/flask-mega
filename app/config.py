from os import environ

class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or 'super-long-secret-keyyyy'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'postgresql+psycopg2://postgres:postgres@localhost:5432/megatut'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ## app-specific
    POSTS_PER_PAGE = 25

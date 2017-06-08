import os


class Configuration(object):
    DEBUG = False
    TESTING = False

    APP_ROOT = os.path.dirname(os.path.realpath(__file__))
    DATABASE = {
        'name': 'database.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    SECRET_KEY = os.getenv('SECRET_KEY', "CHANGEME!!!")
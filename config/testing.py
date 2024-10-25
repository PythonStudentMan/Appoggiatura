# config/testing.py

from .default import *


# Parámetros para activar el modo debug
TESTING = True
DEBUG = True

APP_ENV = APP_ENV_TESTING

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Administrator:Ecnlsnd?2024.@localhost:3306/Appoggiatura'
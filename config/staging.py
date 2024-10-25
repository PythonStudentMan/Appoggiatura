# config/staging.py

from .default import *


APP_ENV = APP_ENV_STAGING

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Administrator:Ecnlsnd?2024.@localhost:3306/Appoggiatura'
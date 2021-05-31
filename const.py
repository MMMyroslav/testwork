import os
from random import randint

SECRET_KEY = os.urandom(randint(32, 64))
SQL_ALCHEMY_DB_URL = "mysql+pymysql://root:12345@127.0.0.1:3306/pjsc"
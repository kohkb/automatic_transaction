import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SQLALCHEMY_TRACK_MODIFICATIONS=True
SQLALCHEMY_DATABASE_URI='sqlite:///fx_trading.db'

DEBUG = True
USERNAME = 'user'
PASSWORD = 'password'
SECRET_KEY = 'secret key'
ACCOUNT_ID = os.environ.get("ACCOUNT_ID")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ENVIRONMENT = os.environ.get("ENVIRONMENT")
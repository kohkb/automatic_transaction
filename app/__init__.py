from flask import Flask

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# config.pyをconfigとして扱うという設定
myapp = Flask(__name__) 
myapp.config.from_object('app.config')

import app.views

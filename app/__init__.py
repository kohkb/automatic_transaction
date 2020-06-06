from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myapp = Flask(__name__) 
myapp.config.from_object('app.config')

db = SQLAlchemy(myapp)

from app.views import views, prices

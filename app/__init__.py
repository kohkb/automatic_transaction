from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myapp = Flask(__name__) 
myapp.config.from_object('app.config')

db = SQLAlchemy(myapp)

from app.views.prices import price
myapp.register_blueprint(price,url_prefix='/users')
from app.views import views, prices

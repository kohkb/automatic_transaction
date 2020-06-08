from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    myapp = Flask(__name__) 
    myapp.config.from_object('app.config')

    if test_config:
        myapp.config.from_mapping(test_config)

    db.init_app(myapp)

    from app.views.views import view
    myapp.register_blueprint(view)

    from app.views.prices import price
    myapp.register_blueprint(price,url_prefix='/users')

    from app.views.api import api
    myapp.register_blueprint(api,url_prefix='/api/v1')

    return myapp


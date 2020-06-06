from flask_script import Command
from app import db

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
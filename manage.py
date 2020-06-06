from flask_script import Manager
from app import myapp

from app.scripts.db import InitDB

if __name__ == "__main__":
    manager = Manager(myapp)
    manager.add_command('init_db', InitDB())
    manager.run()
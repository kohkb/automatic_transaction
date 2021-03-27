from app import create_app
import app.batch 

myapp = create_app()

if __name__ == "__main__":
    myapp.run()

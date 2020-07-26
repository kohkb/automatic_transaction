from app import create_app
from app.services.oanda import Oanda

# TODO move this module to oanda api class
from flask import jsonify

myapp = create_app()

# TODO Refactoring Jobs
import atexit
from apscheduler.scheduler import Scheduler

cron = Scheduler(daemon=True)
cron.start()

@cron.interval_schedule(seconds=5)
def job_function():
  with myapp.app_context():
    oanda = Oanda()
    positions = oanda.positions()
    if positions:
      print("hello world")
      return jsonify({"error": "you already have positions"}), 200
      
    order_price = 100.12
    return oanda.create_order(order_price)    


# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == "__main__":	
  myapp.run()
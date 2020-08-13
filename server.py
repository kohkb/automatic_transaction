from app import create_app
from app.services.fx_transaction import FxTransaction
from app.services.oanda import Oanda
from apscheduler.scheduler import Scheduler
import atexit

myapp = create_app()

# cron setting
cron = Scheduler(daemon=True)
cron.start()

@cron.interval_schedule(seconds=10)
def fx_transcation():
  with myapp.app_context():
    fx_transaction = FxTransaction()
    fx_transaction.execute()

@cron.interval_schedule(seconds=5)
def save_price():
  with myapp.app_context():
    oanda = Oanda()
    oanda.save_price()

atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == "__main__":	
  myapp.run()
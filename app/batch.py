from app import create_app
from app.fx_transaction import FxTransaction
from app.oanda import Oanda
from apscheduler.scheduler import Scheduler
import atexit

myapp = create_app()

# cron setting
cron = Scheduler(daemon=True)
cron.start()

# @cron.interval_schedule(minutes=15)
@cron.interval_schedule(seconds=3)
def save_price():
    with myapp.app_context():
        oanda = Oanda()
        oanda.save_price()


@cron.interval_schedule(minutes=15)
def fx_transcation():
    with myapp.app_context():
        fx_transaction = FxTransaction()
        fx_transaction.execute()

atexit.register(lambda: cron.shutdown(wait=False))
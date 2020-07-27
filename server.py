from app import create_app
from app.services.fx_transaction import FxTransaction
from apscheduler.scheduler import Scheduler
import atexit

myapp = create_app()

# TODO: move another place
# cron setting
cron = Scheduler(daemon=True)
cron.start()

@cron.interval_schedule(seconds=5)
def job_function():
  with myapp.app_context():
    fx_transaction = FxTransaction()
    fx_transaction.execute()

# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == "__main__":	
  myapp.run()
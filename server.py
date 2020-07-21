from app import create_app

myapp = create_app()

# TODO Refactoring Jobs
import atexit
from apscheduler.scheduler import Scheduler

cron = Scheduler(daemon=True)
cron.start()

@cron.interval_schedule(seconds=5)
def job_function():
    print("hello world")

# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == "__main__":	
  myapp.run()
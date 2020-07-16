from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
from app.services.oanda import Oanda
from flask import jsonify
from flask import current_app as myapp

import app.config

def tick():
    print("Tick! The time is : %s'" % datetime.now())

if __name__ == "__main__":	

  scheduler = BlockingScheduler()  # スケジューラを作る
  scheduler.add_job(tick, 'interval', seconds=3)  # ジョブを追加

  print(
      "Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))

  try:
      scheduler.start()  # スタート
  except (KeyboardInterrupt, SystemExit):
      pass

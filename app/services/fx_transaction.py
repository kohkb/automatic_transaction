from app.services.oanda import Oanda
from flask import jsonify

class FxTransaction:
    def __init__(self):
        self.oanda = Oanda()

    def execute(self):
        positions = self.oanda.positions()
        if positions:
            print(jsonify({"error": "you already have positions"}), 200)
            return
      
        order_price = 100.12
        print(self.oanda.create_order(order_price))
from app.services.oanda import Oanda
from flask import current_app as myapp
from flask import jsonify

class FxTransaction:
    def __init__(self):
        self.oanda = Oanda()

    def execute(self):
        if self.has_positions():
            myapp.logger.info('alread has positions')
            return
      
        order_price = self.price()
        print(self.oanda.create_order(order_price))

    def has_positions(self):
        positions = self.oanda.positions()
        return positions['positions'][0]['long']['units'] != '0' or positions['positions'][0]['short']['units'] !='0'

    def price(self):
        # TODO: fetch from Price Class
        return 100.12
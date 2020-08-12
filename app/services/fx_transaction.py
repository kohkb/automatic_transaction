from app.services.oanda import Oanda
from app.services.order_price import OrderPrice
from flask import current_app as myapp

class FxTransaction:
    def __init__(self):
        self.oanda = Oanda()
        self.order_price = OrderPrice()

    def execute(self):
        if self.has_orders():
            myapp.logger.info('alread has orders')
            return
      
        order_price = self.order_price.calculate()
        print(self.oanda.create_order(order_price))

    def has_orders(self):
        return True

    def has_positions(self):
        positions = self.oanda.positions()
        return positions['positions'][0]['long']['units'] != '0' or positions['positions'][0]['short']['units'] !='0'
from app.oanda import Oanda
from app.order_price_manager import OrderPriceManager
from flask import current_app as myapp


class FxTransaction:
    def __init__(self):
        self.oanda = Oanda()
        self.order_price_manager = OrderPriceManager()

    def execute(self):
        if self.has_orders() or self.has_positions():
            myapp.logger.info('alread has orders (positions)')
            return

        order_price = self.order_price_manager.order_price
        stop_loss_price = self.order_price_manager.stop_loss_price
        take_profit_price = self.order_price_manager.take_profit_price

        myapp.logger.info(
            self.oanda.create_order(
                order_price,
                stop_loss_price,
                take_profit_price))

    def has_orders(self):
        orders = self.oanda.orders()
        return orders['orders'] != []

    def has_positions(self):
        positions = self.oanda.positions()
        return positions['positions'][0]['long']['units'] != '0' or positions['positions'][0]['short']['units'] != '0'

from app.models.prices import Price

class OrderPriceManager():
    def __init__(self):
        self.order_price = round(Price.query.order_by(Price.id.desc()).first().ask, 3)
        self.stop_loss_price = round(self.order_price - 0.2, 3)
        self.take_profit_price = round(self.order_price + 0.05, 3)
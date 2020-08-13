from app.models.prices import Price

class OrderPriceManager():
    def __init__(self):
        self.order_price = Price.query.order_by(Price.id.desc()).first().ask
        self.stop_loss_price = self.order_price - 0.2
        self.take_profit_price = self.order_price + 0.05
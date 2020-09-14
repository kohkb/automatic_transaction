from app.models.prices import Price

class OrderPriceManager():
    def __init__(self):
        self.order_price = round(Price.query.order_by(Price.id.desc()).first().ask, 3)

    def stop_loss_price(self):
        return round(self.order_price - 0.2, 3)
    
    def take_profit_price(self):
        return round(self.order_price + 0.05, 3)
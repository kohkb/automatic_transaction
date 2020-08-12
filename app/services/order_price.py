from app.models.prices import Price

class OrderPrice():
    def calculate(self):
        latest_price = Price.query.order_by(Price.id.desc()).first().ask
    
        return latest_price
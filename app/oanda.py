from flask import current_app as myapp
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.positions as positions
from app import db
from app.prices import Price


class Oanda():
    def __init__(self):
        self.api = API(
            access_token=myapp.config['ACCESS_TOKEN'],
            environment=myapp.config['ENVIRONMENT'])
        self.account_id = myapp.config['ACCOUNT_ID']

    def candles(self, instrument="USD_JPY"):
        params = {"count": 1, "granularity": "M5"}  # 5分足
        r = instruments.InstrumentsCandles(
            instrument=instrument, params=params)
        return self.api.request(r)

    def positions(self):
        r = positions.PositionList(self.account_id)
        return self.api.request(r)

    def orders(self):
        r = orders.OrderList(self.account_id)
        return self.api.request(r)

    def save_price(self, instrument="USD_JPY"):
        params = {"instruments": instrument}
        r = pricing.PricingInfo(accountID=self.account_id, params=params)

        result = self.api.request(r)

        price = Price(
            instrument=instrument,
            bid=result["prices"][0]["bids"][0]["price"],
            ask=result["prices"][0]["asks"][0]["price"]
        )

        db.session.add(price)
        db.session.commit()

        return result

    def create_order(
            self,
            order_price,
            stop_loss_price,
            take_profit_price,
            instrument="USD_JPY"):
        data = {
            "order": {
                "price": str(order_price),
                "units": "100",
                "stopLossOnFill": {
                    "timeInForce": "GTC",
                    "price": str(stop_loss_price)
                },
                "takeProfitOnFill": {
                    "timeInForce": "GTC",
                    "price": str(take_profit_price)
                },
                "instrument": instrument,
                "timeInForce": "GTC",
                "type": "LIMIT",
                "positionFill": "DEFAULT"
            }
        }

        r = orders.OrderCreate(accountID=self.account_id, data=data)

        # TODO: Orderテーブルに記録する
        return self.api.request(r)

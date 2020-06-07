from flask import current_app as myapp
from flask import jsonify
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.positions as positions

from app import db
from app.models.prices import Price
import json

# TODO: candlesやpricingはクラスを分けて、必要な値のみ取れるようにする
class Oanda():
    def __init__(self):      
        self.api = API(access_token=myapp.config['ACCESS_TOKEN'], environment=myapp.config['ENVIRONMENT'])
        self.account_id = myapp.config['ACCOUNT_ID']

    def candles(self, instrument):
        # 5分足
        params = {"count": 1, "granularity": "M5"}
        r = instruments.InstrumentsCandles(instrument=instrument, params=params)
        try:
            return self.api.request(r)
        except:
            return jsonify({"error": "an error occurred"})
        
    def pricing(self, instrument="USD_JPY"):
        params = {"instruments": instrument}
        r = pricing.PricingInfo(accountID=self.account_id, params=params)
        try:
            result = self.api.request(r)

            bid = result["prices"][0]["bids"][0]["price"]
            ask = result["prices"][0]["asks"][0]["price"]

            price = Price(
                instrument=instrument,
                bid=bid,
                ask=ask
            )

            db.session.add(price)
            db.session.commit()

            return result
        except:
            return jsonify({"error": "an error occurred"})
    
    def orders(self):
        r = orders.OrderList(self.account_id)
        try:
            return self.api.request(r)
        except:
            return jsonify({"error": "an error occurred"})
    
    def create_order(self):
        # WEBに公開するため、一時的に購入リクエストは停止する
        return jsonify({"error": "an error occurred"})

        current_price = 100.12
        data = {
            "order": {
                "price": current_price,
                "units": "1",
                "stopLossOnFill": {
                    "timeInForce": "GTC",
                    "price": current_price - 0.2
                },
                "takeProfitOnFill": {
                    "timeInForce": "GTC",
                    "price": current_price + 0.05
                },
                "instrument": "USD_JPY",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "positionFill": "DEFAULT"
            }
        }

        # 取引中がすでに存在したらスキップ
        r = orders.OrderCreate(accountID=self.account_id, data=data)

        # TODO: Orderテーブルに記録していく        

        return self.api.request(r)
    
    def positions(self):
        r = positions.PositionList(self.account_id)
        try:
            return self.api.request(r)
        except:
            return jsonify({"error": "an error occurred"})
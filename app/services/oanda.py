from flask import current_app as myapp
from flask import jsonify
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
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
            return jsonify({"error": "invalid authentication"})
    
    def orders(self):
        r = orders.OrderList(self.account_id)
        try:
            return self.api.request(r)
        except:
            return jsonify({"error": "invalid authentication"})
    
    def positions(self):
        r = positions.PositionList(self.account_id)
        try:
            return self.api.request(r)
        except:
            return jsonify({"error": "invalid authentication"})





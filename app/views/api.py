from flask import current_app as myapp
from flask import Blueprint
from app.services.oanda import Oanda

# TODO あとで消す
from flask import jsonify

api = Blueprint('api', __name__)

@api.route('/candles/', methods = ['GET'])
def instruments():
    oanda = Oanda()
    instrument = request.args.get('instrument')
    return oanda.candles(instrument)

@api.route('/pricing/', methods = ['GET'])
def pricing():
    oanda = Oanda()
    return oanda.pricing()

@api.route('/orders/', methods = ['GET'])
def orders():
    oanda = Oanda()
    return oanda.orders()

@api.route('/orders/', methods = ['POST'])
def create_order():
    oanda = Oanda()

    # TODO スケジューラに移動
    positions = oanda.positions()

    if positions:
      return jsonify({"error": "you already have positions"}), 200
    

    order_price = 100.12
    return oanda.create_order(order_price)    

@api.route('/positions/', methods = ['GET'])
def positions():
    oanda = Oanda()
    return oanda.positions()
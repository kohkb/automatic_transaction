from app import myapp

from flask import jsonify, request, make_response
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import os

accountID = os.environ.get("ACCOUNT_ID")
access_token = os.environ.get("ACCESS_TOKEN")
environment = os.environ.get("ENVIRONMENT")

@myapp.route('/', methods = ['GET'])
def root():
    return make_response(jsonify({'success':'success'}),200)

@myapp.route('/instruments/', methods = ['GET'])
def instruments():
    instruments = request.args.get('instruments')
    api = API(access_token=access_token, environment="live")
    params = { "instruments": instruments }
    r = accounts.AccountInstruments(accountID=accountID, params=params)
    return api.request(r)
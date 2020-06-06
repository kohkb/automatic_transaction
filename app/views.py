from flask import request, redirect, url_for, render_template, flash, session
from app import myapp

from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

@myapp.route('/', methods = ['GET'])
def show_entries():
    return render_template('entries/index.html')

@myapp.route('/login', methods=['GET', 'POST'])
def loging():
    if request.method == 'POST':
        if request.form['username'] != myapp.config['USERNAME']:
            print('ユーザ名が異なります')
        elif request.form['password'] != myapp.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            return redirect('/')
    return render_template('login.html')

@myapp.route('/logout')
def logout():
    return redirect('/')

@myapp.route('/api/v1/instruments/', methods = ['GET'])
def instruments():
    instruments = request.args.get('instruments')
    api = API(access_token=myapp.config['ACCESS_TOKEN'], environment=myapp.config['ACCESS_TOKEN'])
    params = { "instruments": instruments }
    r = accounts.AccountInstruments(accountID=myapp.config['ACCOUNT_ID'], params=params)
    return api.request(r)
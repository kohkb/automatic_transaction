from flask import request, redirect, url_for, render_template, flash, session
from app import myapp
from functools import wraps

from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

@myapp.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('login'))

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

@myapp.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['username'] != myapp.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != myapp.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました。')
            return redirect(url_for('price.show_prices'))
    return render_template('login.html')

@myapp.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました。')
    return redirect(url_for('price.show_prices'))

@myapp.route('/api/v1/instruments/', methods = ['GET'])
def instruments():
    instruments = request.args.get('instruments')
    api = API(access_token=myapp.config['ACCESS_TOKEN'], environment=myapp.config['ACCESS_TOKEN'])
    params = { "instruments": instruments }
    r = accounts.AccountInstruments(accountID=myapp.config['ACCOUNT_ID'], params=params)
    return api.request(r)
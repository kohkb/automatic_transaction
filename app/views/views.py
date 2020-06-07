from flask import request, redirect, url_for, render_template, flash, session
from flask import current_app as myapp
from functools import wraps
from flask import Blueprint
from app.services.oanda import Oanda

from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.accounts as accounts

view = Blueprint('view', __name__)

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('view.login'))
        return view(*args, **kwargs)
    return inner

@view.route('/login', methods=['GET', 'POST'])
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

@view.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました。')
    return redirect(url_for('price.show_prices'))

# TODO: APIはファイルを分ける
@view.route('/api/v1/candles/', methods = ['GET'])
def instruments():
    instrument = request.args.get('instrument')
    oanda = Oanda()
     
    return oanda.candles(instrument)

@view.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('view.login'))
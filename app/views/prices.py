from flask import request, redirect, url_for, render_template, flash, session
from app.models.prices import Price
from app import myapp
from app import db

@myapp.route('/', methods = ['GET'])
def show_prices():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    prices = Price.query.order_by(Price.id.desc()).all()
    
    return render_template('prices/index.html', prices=prices)

@myapp.route('/prices/new', methods = ['GET'])
def new_price():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('prices/new.html')


@myapp.route('/prices/', methods = ['POST'])
def add_price():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    print('hello world')
    print(request.form)
    price = Price(
        instrument=request.form['instrument'],
        bid=request.form['bid'],
        ask=request.form['ask']
    )
    print('hello world')

    db.session.add(price)
    db.session.commit()
    flash('レートが保存されました')
    return redirect(url_for('show_prices'))
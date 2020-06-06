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
    price = Price(
        instrument=request.form['instrument'],
        bid=request.form['bid'],
        ask=request.form['ask']
    )

    db.session.add(price)
    db.session.commit()
    flash('レートが保存されました')
    return redirect(url_for('show_prices'))

@myapp.route('/prices/<int:id>', methods=['GET'])
def show_price(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    price = Price.query.get(id)
    return render_template('prices/show.html', price=price)

@myapp.route('/prices/<int:id>/edit', methods=['GET'])
def edit_price(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    price = Price.query.get(id)
    return render_template('prices/edit.html', price=price)

@myapp.route('/prices/<int:id>/update', methods=['POST'])
def update_price(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    price = Price.query.get(id)
    price.instrument=request.form['instrument']
    price.bid=request.form['bid']
    price.ask=request.form['ask']

    db.session.merge(price)
    db.session.commit()
    flash('レートが更新されました')
    return redirect(url_for('show_prices'))

@myapp.route('/prices/<int:id>/delete', methods=['POST'])
def delete_price(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    price = Price.query.get(id)

    db.session.delete(price)
    db.session.commit()
    flash('レートが削除されました')
    return redirect(url_for('show_prices'))
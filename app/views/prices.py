from flask import request, redirect, url_for, render_template, flash, session
from flask import current_app as myapp
from app import db
from app.prices import Price
from app.views.views import login_required
from flask import Blueprint

price = Blueprint('price', __name__)


@price.route('/', methods=['GET'])
@login_required
def show_prices():
    prices = Price.query.order_by(Price.id.desc()).all()
    return render_template('prices/index.html', prices=prices)


@price.route('/prices/new', methods=['GET'])
@login_required
def new_price():
    return render_template('prices/new.html')


@price.route('/prices/', methods=['POST'])
@login_required
def add_price():
    price = Price(
        instrument=request.form['instrument'],
        bid=request.form['bid'],
        ask=request.form['ask']
    )

    db.session.add(price)
    db.session.commit()
    flash('レートが保存されました')
    return redirect(url_for('price.show_prices'))


@price.route('/prices/<int:id>', methods=['GET'])
@login_required
def show_price(id):
    price = Price.query.get(id)
    return render_template('prices/show.html', price=price)


@price.route('/prices/<int:id>/edit', methods=['GET'])
@login_required
def edit_price(id):
    price = Price.query.get(id)
    return render_template('prices/edit.html', price=price)


@price.route('/prices/<int:id>/update', methods=['POST'])
@login_required
def update_price(id):
    price = Price.query.get(id)
    price.instrument = request.form['instrument']
    price.bid = request.form['bid']
    price.ask = request.form['ask']

    db.session.merge(price)
    db.session.commit()
    flash('レートが更新されました')
    return redirect(url_for('price.show_prices'))


@price.route('/prices/<int:id>/delete', methods=['POST'])
@login_required
def delete_price(id):
    price = Price.query.get(id)

    db.session.delete(price)
    db.session.commit()
    flash('レートが削除されました')
    return redirect(url_for('price.show_prices'))

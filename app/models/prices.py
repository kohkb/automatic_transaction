from app import db
from datetime import datetime, timezone, timedelta

# TODO: 別のファイルに移動して共通化する
JST = timezone(timedelta(hours=+9), 'JST')

class Price(db.Model):
    __table_name__ = 'prices'
    id = db.Column(db.Integer, primary_key=True)
    instrument = db.Column(db.String(10))
    bid = db.Column(db.Float)
    ask = db.Column(db.Float)
    created_at = db.Column(db.DateTime)

    def __init__(self, instrument=None, bid=None, ask=None):
        self.instrument = instrument
        self.bid = bid
        self.ask = ask
        self.created_at = datetime.now(JST)
    
    def __repr__(self):
        return '<Price id:{} instrument: {} bid: {} ask: {} '.format(self.id, self.instrument, self.bid, self.ask)
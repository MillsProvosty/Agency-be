from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True)
    last_name = db.Column(db.String(120), index=True)
    pronouns = db.Column(db.String(120))
    language = db.Column(db.String(120))
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.Integer, index=True, unique=True)
    password_hash = db.Column(db.String(128))
    opportunities = db.relationship('Opportunity', backref='client', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.first_name)

class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    type = db.Column(db.String(120), index=True)
    location = db.Column(db.String(120), index=True)
    estimated_time = db.Column(db.String(120), index=True)
    description = db.Column(db.String(140), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Opportunity {}>'.format(self.body)

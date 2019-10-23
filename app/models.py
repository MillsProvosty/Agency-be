from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True)
    last_name = db.Column(db.String(120), index=True)
    pronouns = db.Column(db.String(120))
    language = db.Column(db.String(120))
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.Integer, index=True, unique=True)
    password_hash = db.Column(db.String(128))
    opportunities = db.relationship('Opportunity', backref='client', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def __repr__(self):
        return '<User {}>'.format(self.first_name)

    def to_dict(self, include_email=False):
        data = {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'email': self.email,
        'phone_number': self.phone_number
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['first_name', 'last_name', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password_hash' in data:
            self.set_password(data['password_hash'])

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

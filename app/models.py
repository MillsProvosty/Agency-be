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

    def __repr__(self):
        return '<User {}>'.format(self.first_name)

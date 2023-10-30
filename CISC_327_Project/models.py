# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    addresses = db.relationship('Address', backref='user', cascade='all,delete', lazy='dynamic')
    payment_methods = db.relationship('Payment_Method', backref='user', cascade='all,delete',lazy='dynamic')
    def __repr__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}, Address: {self.addresses.filter_by(default=True).all()}"

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    default = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Payment_Method(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_num = db.Column(db.String(16), nullable=False)
    default = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    cuisine = db.Column(db.String(20), unique=True, nullable=False)
    item_list = db.relationship('Item', backref='restaurant', cascade='all,delete', lazy=True)
    favourites_list = db.relationship('Favourites',backref='restaurant', cascade='all,delete', lazy=True)
    def __repr__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Address: {self.address}"
    
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), unique=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    favourites_id = db.Column(db.Integer, db.ForeignKey('favourites.id'), nullable=False)

class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_list = db.relationship('Item', backref='favourites', lazy=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    
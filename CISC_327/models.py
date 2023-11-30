# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model, UserMixin): # user table
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    addresses = db.relationship('Address', backref='user', cascade='all,delete', lazy='dynamic') # can filter, delete related addresses to user when user is deleted
    payment_methods = db.relationship('Payment_Method', backref='user', cascade='all,delete',lazy='dynamic') # same for this column
    def __repr__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}, Address: {self.addresses.filter_by(default=True).all()}"

class Address(db.Model): # address table, linked to a given user
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    default = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Payment_Method(db.Model): # payment method table, linked to a given user
    __tablename__ = 'payment_method'
    id = db.Column(db.Integer, primary_key=True)
    card_num = db.Column(db.String(16), nullable=False)
    default = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Restaurant(db.Model): # restaurant table, associated to a list of items
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    cuisine = db.Column(db.String(20), nullable=False)
    item_list = db.relationship('Item', backref='restaurant', cascade='all,delete', lazy='dynamic') # can filter, delete related items when restaurant is deleted
    def __repr__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}, Address: {self.address}, Item List: {self.item_list.filter_by().all()}, Cuisine: {self.cuisine}"
    
class Item(db.Model): # item table, associated with a restaurant
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    description = db.Column(db.Text(), unique=True, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    in_cart = db.Column(db.Boolean, nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}, Quantity: {self.quantity}."


# Add_To_Cart.py
# Author: Unbearable Solutions
from flask import Blueprint, request, redirect, url_for, flash
from ...models import db, Item
from flask_login import login_required
add_to_cart_blueprint = Blueprint('add_to_cart',__name__)
@add_to_cart_blueprint.route("/add_to_cart/<item_id>/<restaurant_id>",methods=['POST'])

# Function for when add to cart button is pressed
def add_to_cart(item_id, restaurant_id):
    if request.method=='POST': # Checks if form was submitted
        item = Item.query.get(item_id) # Gets the specified item from the database
        if not item: # Error checking to see if specified item can be found in the database
            flash("Item Not Found.",'danger')
        else:
            item.in_cart = True # Changes the attribute in the database
            db.session.commit()
            flash(f"{item.name} added to cart!", 'success')
        return redirect(url_for('menu.menu',restaurant_id=restaurant_id)) # Reloads the restaurant's menu page
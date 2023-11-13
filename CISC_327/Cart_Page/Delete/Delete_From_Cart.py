# Delete_From_Cart.py
# Author: Unbearable Solutions
from flask import Blueprint, request, redirect, url_for, flash
from models import db, Item
from flask_login import login_required
delete_from_cart_blueprint = Blueprint('delete_from_cart',__name__)
@delete_from_cart_blueprint.route('/delete_from_cart/<item_id>/<restaurant_id>', methods=['POST'])

# Function for when remove from cart button is pressed 
def delete_from_cart(item_id, restaurant_id):
    if request.method=='POST': 
        item = Item.query.get(item_id) # Gets specified item
        if not item: # Error checking to make sure item is in database
            flash("Item Not Found",'danger')
        else:
            item.in_cart = False # Changes attribute in the database
            db.session.commit()
            flash(f"{item.name} deleted from cart!",'success')
        return redirect(url_for('cartpage.cartpage', restaurant_id=restaurant_id)) # Reloads the cartpage

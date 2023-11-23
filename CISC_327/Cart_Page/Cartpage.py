from flask import Blueprint, redirect, url_for, render_template, flash, session
from ..models import Item, Restaurant
from .Subtotal import Subtotal
from flask_login import current_user, login_required
cartpage_blueprint = Blueprint('cartpage',__name__)
@cartpage_blueprint.route("/cartpage/<restaurant_id>", methods=['GET','POST'])
@login_required
def cartpage(restaurant_id):
    subtotal = Subtotal.subtotal()
    cart_items = Item.query.filter_by(in_cart=True).all() # Gets all the items that have been added to the cart
    if not cart_items:
        return redirect(url_for('homepage.homepage')) # Redirects back to homepage if there are no cart items
    else:
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant: # Error checking to see if restaurant can be found
            flash(f'Restaurant not found','danger')
        return render_template("cartpage.html", cart_items=cart_items, subtotal=subtotal, restaurant=restaurant)
    
@cartpage_blueprint.route("/edit_quantity/<item_id>/<restaurant_id>/<q>", methods=['GET', 'POST'])
def edit_quantity(item_id, restaurant_id, q):
    item = Item.query.filter_by(id=item_id)
    session[item_id] = item.price * q
    return url_for('cartpage.cartpage', restaurant_id=restaurant_id)
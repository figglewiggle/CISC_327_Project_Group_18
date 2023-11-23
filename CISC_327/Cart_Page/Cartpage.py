from flask import Blueprint, redirect, url_for, render_template, flash
from ..models import Item, Restaurant
from .Subtotal import Subtotal
from flask_login import current_user, login_required
cartpage_blueprint = Blueprint('cartpage',__name__)
@cartpage_blueprint.route("/cartpage/<restaurant_id>", methods=['GET','POST'])
@login_required
def cartpage(restaurant_id):
    subtotal = Subtotal.subtotal()
    msg=""
    cart_items = Item.query.filter_by(in_cart=True).all() # Gets all the items that have been added to the cart
    if not cart_items:
        msg="You have not added any items to your cart."
        return redirect(url_for('homepage.homepage')) # Redirects back to homepage if there are no cart items
    else:
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant: #Error checking to see if restaurant can be found
            flash(f'Restaurant not found','danger')
        return render_template("cartpage.html", cart_items=cart_items, subtotal=subtotal, restaurant=restaurant, msg=msg)


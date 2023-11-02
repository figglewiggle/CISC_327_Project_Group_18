from flask import Blueprint, redirect, url_for, render_template, flash
from models import Item, Restaurant
from flask_login import current_user, login_required
cartpage_blueprint = Blueprint('cartpage',__name__)
@cartpage_blueprint.route("/cartpage/<restaurant_id>", methods=['GET','POST'])
@login_required
def cartpage(restaurant_id):
    subtotal = 0
    msg=""
    cart_items = Item.query.filter_by(in_cart=True).all()
    if not cart_items:
        return redirect(url_for('homepage.homepage'))
    else:
        for c in cart_items:
            subtotal += c.price
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            flash(f'Restaurant not found','danger')
        return render_template("cartpage.html", cart_items=cart_items, subtotal=subtotal, restaurant=restaurant)

from flask import Blueprint, render_template, request, flash
from models import Item, Restaurant
from flask_login import current_user
checkout_blueprint = Blueprint('checkout',__name__)
@checkout_blueprint.route("/checkout/<restaurant_id>", methods=['GET','POST'])
def checkout(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        flash(f'Restaurant not found','danger')
    subtotal = 0
    cart_items = Item.query.filter(Item.in_cart==True).all()
    if current_user.is_authenticated:
        name = current_user.name
        email = current_user.email
        phone_number = current_user.phone_number
        address = current_user.addresses.filter_by(default=True).first()
        payment_method = current_user.payment_methods.filter_by(default=True).first()
    for c in cart_items:
        subtotal += c.price
    tax = subtotal*0.14
    total = tax + subtotal
    return render_template("checkout.html", restaurant=restaurant,cart_items=cart_items,subtotal=subtotal,total=total,tax=tax,name=name,email=email,phone_number=phone_number,address=address,payment_method=payment_method)
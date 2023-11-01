from flask import Blueprint, render_template, request
from models import db, Item
cartpage_blueprint = Blueprint('cartpage',__name__)
@cartpage_blueprint.route("/cartpage", methods=['GET','POST'])
def cartpage():
    subtotal = 0
    msg = ""
    cart_items = Item.query.filter(Item.in_cart==True).all()
    if not cart_items:
        msg="You haven't added any items to your cart yet."
    for c in cart_items:
        subtotal += c.price
    return render_template("cartpage.html", cart_items=cart_items, subtotal=subtotal, msg=msg)

from flask import Blueprint, render_template, request
from models import db, Item
cartpage_blueprint = Blueprint('cartpage',__name__)
@cartpage_blueprint.route("/cartpage", methods=['GET','POST'])
def cartpage():
    cart_items = Item.query.filter_by(in_cart=True).all()
    return render_template("cartpage.html", cart_items=cart_items)
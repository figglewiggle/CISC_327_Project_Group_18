from flask import Blueprint, render_template, request
from models import db, Item
cartpage_blueprint = Blueprint('cartpage',__name__)
@cartpage_blueprint.route("/cartpage", methods=['GET','POST'])
def cartpage():
    """cart_items = db.session.query(Item).filter(Item.in_cart==True).all()
    names = []
    for c in cart_items:
        names.append(c.name)"""
    return render_template("cartpage.html")
# Add_To_Cart.py
# Author: Unbearable Solutions
from flask import Blueprint, request, redirect, url_for, flash
from models import Item
from flask_login import login_required
add_to_cart_blueprint = Blueprint('add_to_cart',__name__)
@add_to_cart_blueprint.route("/add_to_cart/<int:item_id>",methods=['POST'])
@login_required
def add_to_cart(item_id):
    if request.method=='POST':
        item = Item.query.get(item_id)
        if not item:
            flash("Item Not Found.",'danger')
            return redirect(url_for('menu.menu'))
        item.in_cart = True
        flash(f"{item.name} added to cart!", 'success')
        return redirect(url_for('menu.menu'))
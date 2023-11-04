from flask import Blueprint, redirect, url_for, render_template, flash, request, session
from models import Item, Restaurant
import Cart_Page.Subtotal.Subtotal as Subtotal
from flask_login import current_user, login_required
tips_blueprint = Blueprint('tips',__name__)
@tips_blueprint.route("/tips/<restaurant_id>", methods=['GET','POST'])
@login_required
def tips(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        flash(f'Restaurant not found','danger')
    if request.method=="POST":
        tip = request.form['tip']
        session['tip'] = tip
    return redirect(url_for('checkout.checkout', restaurant_id=restaurant_id))

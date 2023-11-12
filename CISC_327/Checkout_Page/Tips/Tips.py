from flask import Blueprint, redirect, url_for, render_template, flash, request, session
from models import Item, Restaurant
import Cart_Page.Subtotal.Subtotal as Subtotal
from flask_login import current_user, login_required
tips_blueprint = Blueprint('tips',__name__)
@tips_blueprint.route("/tips/<restaurant_id>", methods=['GET','POST'])
@login_required
# Function handles when "add tip" button is pressed
def tips(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant: # Error checking to make sure restaurant is in database
        flash(f'Restaurant not found','danger')
    if request.method=="POST":
        tip = request.form['tip'] # Gets the tip amount that the user inputted
        session['tip'] = tip # Stores it in session
    return redirect(url_for('checkout.checkout', restaurant_id=restaurant_id)) # Reloads checkout page

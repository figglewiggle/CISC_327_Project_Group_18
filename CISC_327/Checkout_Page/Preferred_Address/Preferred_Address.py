from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from models import db, bcrypt, Restaurant

preferred_address_blueprint = Blueprint('preferred_address', __name__)
@preferred_address_blueprint.route("/preferred_address/<restaurant_id>", methods=['GET', 'POST'])
@login_required
def preferred_address(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        flash(f'Restaurant not found','danger')
    if request.method == 'POST':
        new_address = request.form['change_address']
        
        db.session.commit()
        return redirect(url_for('checkout.checkout', restaurant_id=restaurant_id))
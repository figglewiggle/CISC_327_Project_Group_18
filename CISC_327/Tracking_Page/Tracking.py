from flask import Blueprint, redirect, url_for, render_template, flash, session
from ..models import Item, Restaurant
from flask_login import current_user, login_required
tracking_blueprint = Blueprint('tracking',__name__)
@tracking_blueprint.route("/tracking/<restaurant_id>", methods=['GET','POST'])
@login_required
def tracking(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant: # Error checking
        flash(f'Restaurant not found','danger')
    else:
        
        return render_template("tracking.html")
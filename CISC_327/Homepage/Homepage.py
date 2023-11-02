from flask import Blueprint, render_template, session
from models import Restaurant
from flask_login import current_user, login_required
homepage_blueprint = Blueprint('homepage',__name__)
@homepage_blueprint.route("/homepage", methods=['GET','POST'])
@login_required
def homepage():
    selected_cuisine = session.pop('selected_cuisine', None)
    if selected_cuisine:
        restaurants = Restaurant.query.filter_by(cuisine=selected_cuisine).all()
    else:
        restaurants = Restaurant.query.filter_by().all()
    if current_user.is_authenticated:
        default_address = current_user.addresses.filter_by(default=True).first()
    return render_template("homepage.html",restaurants=restaurants,default_address=default_address)
    
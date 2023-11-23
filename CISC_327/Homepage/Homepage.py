from flask import Blueprint, render_template, session
from ..models import db, Restaurant, Address
from flask_login import current_user, login_required
homepage_blueprint = Blueprint('homepage',__name__)
@homepage_blueprint.route("/homepage", methods=['GET','POST'])
@login_required
def homepage():
    selected_cuisine = session.pop('selected_cuisine', None) # checks to see if a filter search was applied
    if selected_cuisine: # if so, filter
        restaurants = Restaurant.query.filter_by(cuisine=selected_cuisine).all()
    else:
        restaurants = Restaurant.query.filter_by().all() # if not, just show all restaurants
    if current_user.is_authenticated:
        default_address = None
        if len(current_user.addresses.filter_by().all())==1: # if only one address left
            addresses = current_user.addresses.all()
            default_address = addresses[0]
            if not default_address.default: # and it is not default
                default_address.default = True # make it default
                db.session.commit()
        else:
            default_address = current_user.addresses.filter_by(default=True).first()
    return render_template("homepage.html",restaurants=restaurants,default_address=default_address) # display restaurants and default address
    
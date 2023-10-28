from flask import Blueprint, render_template
from Objects import Restaurant, Item
from flask_login import current_user, login_required
homepage_blueprint = Blueprint('homepage',__name__)
restaurants = [Restaurant("Jack Astor's","4167346758","145 Division Street",
                          ["American"],[Item("Chicken Fingers",6.49, "Yummy"),Item("Poutine",7.99, "Yummy More")],[Item("Chicken Fingers",6.49,"Yummy")])]
@homepage_blueprint.route("/homepage", methods=['GET','POST'])
@login_required
def homepage():
    if current_user.is_authenticated:
        default_address = current_user.addresses.filter_by(default=True).first()
    return render_template("homepage.html",restaurants=restaurants,default_address=default_address)
    
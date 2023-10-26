from flask import Blueprint, render_template, request
from Objects import Restaurant, Item
from flask_login import login_required, current_user
from models import User
homepage_blueprint = Blueprint('homepage',__name__)
restaurants = [Restaurant("Jack Astor's","4167346758","145 Division Street",
                          ["American"],[Item("Chicken Fingers",6.49, "Yummy"),Item("Poutine",7.99, "Yummy More")],[Item("Chicken Fingers",6.49,"Yummy")])]
@homepage_blueprint.route("/homepage", methods=['GET','POST'])
@login_required
def homepage():
    return render_template("homepage.html",restaurants=restaurants,address=current_user.addresses.filter_by(default=True).all())
    
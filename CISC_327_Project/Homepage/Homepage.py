from flask import Blueprint, render_template, request
from Objects import Restaurant, Item
homepage_blueprint = Blueprint('homepage',__name__)
restaurants = [Restaurant("Jack Astor's","4167346758","145 Division Street",
                          ["American","Canadian"],[Item("Chicken Fingers",6.49, "Yummy"),Item("Poutine",7.99, "Yummy More")],[Item("Chicken Fingers",6.49,"Yummy")])]
@homepage_blueprint.route("/homepage", methods=['GET','POST'])
def homepage():
    return render_template("homepage.html",restaurants=restaurants)
    
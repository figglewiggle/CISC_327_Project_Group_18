# Menu_Access.py
from flask import Blueprint, render_template
menu_blueprint = Blueprint('menu',__name__)
@menu_blueprint.route("/menu/<restaurant_name>", methods=['GET','POST'])
def menu(restaurant_name):
    return render_template("menupage.html", restaurant_name = restaurant_name)
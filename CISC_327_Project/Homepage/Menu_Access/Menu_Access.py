# Menu_Access.py
from flask import Blueprint
menu_blueprint = Blueprint('menu',__name__)
@menu_blueprint.route("homepage/<restaurant_name>/menu", methods=['GET','POST'])
def menu(restaurant_name):
    return f"Menu for {restaurant_name}"
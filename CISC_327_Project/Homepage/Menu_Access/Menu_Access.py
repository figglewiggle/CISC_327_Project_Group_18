# Menu_Access.py
from flask import Blueprint, render_template
menu_blueprint = Blueprint('menu',__name__)
@menu_blueprint.route("/menu", methods=['GET','POST'])
def menu():
    return render_template("menupage.html")
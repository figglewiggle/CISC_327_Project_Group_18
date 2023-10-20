from flask import Blueprint, render_template, request
cartpage_blueprint = Blueprint('cartpage',__name__)
@cartpage_blueprint.route("/cartpage", methods=['GET','POST'])
def cartpage():
    return render_template("cartpage.html")
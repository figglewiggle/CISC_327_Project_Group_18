from flask import Blueprint, render_template, request
homepage_blueprint = Blueprint('homepage',__name__)
@homepage_blueprint.route("/homepage", methods=['GET','POST'])
def homepage():
    return render_template("homepage.html")
    
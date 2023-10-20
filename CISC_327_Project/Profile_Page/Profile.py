from flask import Blueprint, render_template, request
profile_blueprint = Blueprint('profile', __name__)
@profile_blueprint.route("/profile", methods = ['GET', 'POST'])
def profile():
    return render_template("Profile.html")
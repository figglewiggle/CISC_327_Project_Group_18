# Edit_Password.py
from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from models import db, bcrypt

edit_password_blueprint = Blueprint('edit_password', __name__)

@edit_password_blueprint.route("/edit_password", methods=['GET', 'POST'])
@login_required
def edit_password():
    if request.method == 'POST': # if form is submitted
        new_password = request.form['new_password'] # get password
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8') # hash password
        current_user.password = hashed_password # update password
        db.session.commit()
        return redirect(url_for('profile.profile'))

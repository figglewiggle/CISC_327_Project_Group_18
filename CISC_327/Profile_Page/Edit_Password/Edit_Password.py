# Edit_Password.py
from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from models import db, bcrypt

edit_password_blueprint = Blueprint('edit_password', __name__)

@edit_password_blueprint.route("/edit_password", methods=['GET', 'POST'])
@login_required
def edit_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        current_user.password = hashed_password
        db.session.commit()
        return redirect(url_for('profile.profile'))

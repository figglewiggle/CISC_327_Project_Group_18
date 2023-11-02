# Edit_Password.py
from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from models import db, bcrypt

edit_password_blueprint = Blueprint('edit_password', __name__)

@edit_password_blueprint.route("/edit_password", methods=['GET', 'POST'])
@login_required
def edit_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        if bcrypt.check_password_hash(current_user.password, current_password):
            hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            current_user.password = hashed_password
            db.session.commit()
            flash('Your password has been updated.', 'success')
        else:
            flash('Current password is incorrect.', 'danger')
        return redirect(url_for('profile.profile'))

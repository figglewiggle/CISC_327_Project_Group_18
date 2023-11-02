from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from models import db, bcrypt

edit_phone_blueprint = Blueprint('edit_phone', __name__)
@edit_phone_blueprint.route("/edit_phone", methods=['GET', 'POST'])
@login_required
def edit_phone():
    if request.method == 'POST':
        new_phone = request.form['new_phone']
        current_user.phone_number = new_phone
        db.session.commit()
        return redirect(url_for('profile.profile'))

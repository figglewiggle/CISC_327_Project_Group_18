from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from ...models import db, bcrypt

edit_phone_blueprint = Blueprint('edit_phone', __name__)
@edit_phone_blueprint.route("/edit_phone", methods=['GET', 'POST'])
@login_required # user has to be logged to access this functionality
def edit_phone():
    if request.method == 'POST': # if form is submitted
        new_phone = request.form['new_phone']
        if new_phone: # if what's submitted is non-empty
            current_user.phone_number = new_phone # update phone number
            db.session.commit()
        return redirect(url_for('profile.profile'))

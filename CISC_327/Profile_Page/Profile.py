from flask import Blueprint, render_template, request, redirect
from flask_login import current_user,login_required
from ..models import db, bcrypt
profile_blueprint = Blueprint('profile', __name__)
@profile_blueprint.route("/profile", methods = ['GET', 'POST'])
@login_required
def profile():
    if current_user.is_authenticated:
        if request.method == 'POST': # if a form as been submitted
            field_to_edit = request.form.get('field_to_edit') # get the edited item
            if field_to_edit == request.form.get('phone_number'): # if it is the phone number that has been edited
                updated_phone_number = request.form['phone_number']
                current_user.phone_number = updated_phone_number # update
            if field_to_edit == request.form.get('password'): # edited password
                updated_password = request.form['password']
                hashed_password = bcrypt.generate_password_hash(updated_password).decode('utf-8')
                current_user.password = hashed_password # update
            db.session.commit()
            return redirect('/profile')
        name = current_user.name # otherwise just get the current attributes and display them
        email = current_user.email
        phone_number = current_user.phone_number
        password = current_user.password
        addresses = current_user.addresses
        payment_methods = current_user.payment_methods
    return render_template("Profile.html",name=name,email=email,phone_number=phone_number, password=password, addresses=addresses, payment_methods=payment_methods)


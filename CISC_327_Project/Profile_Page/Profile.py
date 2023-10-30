'''
from flask import Blueprint, render_template
from flask_login import current_user,login_required
profile_blueprint = Blueprint('profile', __name__)
@profile_blueprint.route("/profile", methods = ['GET', 'POST', 'PUT'])
@login_required
def profile():
    if current_user.is_authenticated:
        name = current_user.name
        email = current_user.email
        phone_number = current_user.phone_number
        password = current_user.password
        addresses = current_user.addresses
        payment_methods = current_user.payment_methods
        if request.method == 'PUT':
            updated_phone_number = request.form['phone number']
            updated_password = request.form['password']
            #hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            updated_address = request.form['address']
            current_user.phone_number = updated_phone_number
            current_user.password = updated_password
            current_user.address = updated_address
            db.session.commit()
            return redirect('/profile')
    return render_template("Profile.html",name=name,email=email,phone_number=phone_number, password=password, addresses=addresses, payment_methods=payment_methods)
'''
from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
from models import User, db, bcrypt  # Remove the import for Address if addresses are stored as strings

profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if current_user.is_authenticated:
        if request.method == 'POST':
            field_to_edit = request.form.get('field_to_edit')

            if field_to_edit == 'phone_number':
                new_phone_number = request.form.get('phone_number')
                current_user.phone_number = new_phone_number
            elif field_to_edit == 'new_password':
                new_password = request.form.get('new_password')
                hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
                current_user.password = hashed_password
            # Add similar conditions for other fields as needed

            # Save changes to the database
            db.session.commit()
            return redirect('/profile')

        # Fetch user details
        name = current_user.name
        email = current_user.email
        phone_number = current_user.phone_number
        addresses = current_user.addresses  # Assuming 'addresses' is a list of strings in the User model
        payment_methods = current_user.payment_methods

        return render_template("Profile.html", name=name, email=email, phone_number=phone_number,
                               addresses=addresses, payment_methods=payment_methods)


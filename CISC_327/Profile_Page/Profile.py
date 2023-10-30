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


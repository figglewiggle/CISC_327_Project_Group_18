
from flask import Blueprint, render_template
from flask_login import current_user,login_required
profile_blueprint = Blueprint('profile', __name__)
@profile_blueprint.route("/profile", methods = ['GET', 'POST'])
@login_required
def profile():
    if current_user.is_authenticated:
        name = current_user.name
        email = current_user.email
        phone_number = current_user.phone_number
        password = current_user.password
        addresses = current_user.addresses
        payment_methods = current_user.payment_methods
    return render_template("Profile.html",name=name,email=email,phone_number=phone_number, password=password, addresses=addresses, payment_methods=payment_methods)
"""
from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_required

profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        if current_user.is_authenticated:
            # Access the form data sent via POST request
            updated_email = request.form.get('email')
            updated_phone_number = request.form.get('phone')
            updated_password = request.form.get('password')
            
            # Update the user's information in the database
            # Example: (assuming you're using SQLAlchemy)
            user = current_user  # Assuming you have a User model
            user.email = updated_email
            user.phone_number = updated_phone_number
            # Update other fields as needed (e.g., password update needs hashing)

            # Commit the changes to the database
            db.session.commit()

            # Redirect to the profile page or a success page
            return redirect('/profile')  # Redirect to the profile page

    # The rest of your GET method logic remains the same
    # Fetch user data and render the profile template
    # ...

    return render_template("Profile.html", name=current_user.name, email=current_user.email, phone_number=current_user.phone_number, password=current_user.password, addresses=current_user.addresses, payment_methods=current_user.payment_methods)
"""
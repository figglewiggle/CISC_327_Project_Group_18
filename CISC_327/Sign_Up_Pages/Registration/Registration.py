# Registration.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, bcrypt, User, Address, Payment_Method, Item
registration_blueprint = Blueprint('registration', __name__)
@registration_blueprint.route("/registration", methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST': # if registration form was submitted
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') # generate password hash for security
        address = request.form['address']
        payment_method = request.form['payment_method']
        with open('Sign_Up_Pages\Registration\Registration.txt', 'a') as file: # write registration info for testing purposes
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Password: {password}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Payment Method: {payment_method}\n")
        user = User(name=name,email=email,phone_number=phone_number,password=hashed_password) # make a new user row
        address_col = Address(address=address,default=True) # make a new address row
        payment_method_col = Payment_Method(card_num=payment_method,default=True) # make a new payment method row
        user.addresses.append(address_col) # make the new address row's user_id attribute the current user id
        user.payment_methods.append(payment_method_col) # same as above but for payment method row
        try:
            db.session.add(user)
            db.session.commit()
            flash('User registered.','success')
            return redirect(url_for('homepage.homepage'))
        except Exception as e: # if errors occur whilst registering user
            db.session.rollback() # rollback changes to the database above
            print(e)
            flash(f'Error registering user', 'danger')
            return render_template('registration.html')
    return render_template('registration.html')



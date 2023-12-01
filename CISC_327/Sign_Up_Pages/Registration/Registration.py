# Registration.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ...models import db, bcrypt, User, Address, Payment_Method, Item
import os
import re
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

        # Validate email format
        email_pattern = re.compile(r'^[a-zA-Z0-9]+@(gmail\.com|yahoo\.com|hotmail\.com)$')
        if not email_pattern.match(email) or len(email)>20:
            flash('Invalid email format. Please use a valid email address.', 'danger')
            return render_template('registration.html')
        
        phone_pattern = re.compile(r'^[0-9]+$')
        if not phone_pattern.match(phone_number) or len(phone_number)!=10:
            flash('Invalid phone format. Please use a valid phone number.', 'danger')
            return render_template('registration.html')
         
        address_pattern = re.compile(r'^[a-zA-Z0-9 ]+$')
        if not address_pattern.match(address) or len(address)>50:
            flash('Invalid address format. Please use a valid address.', 'danger')
            return render_template('registration.html')
        
        payment_pattern = re.compile(r'^[0-9]+$')
        if not payment_pattern.match(payment_method) or len(payment_method)!=16:
            flash('Invalid payment method format. Please use a valid payment method.', 'danger')
            return render_template('registration.html')

        file_path = os.path.join(os.path.dirname(__file__),'Registration.txt')
        with open(file_path, 'a') as file: # write registration info for testing purposes
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
            return redirect(url_for('login.login'))
        except Exception as e: # if errors occur whilst registering user
            db.session.rollback() # rollback changes to the database above
            print(e)
            flash(f'Error registering user', 'danger')
            return render_template('registration.html')
    return render_template('registration.html')



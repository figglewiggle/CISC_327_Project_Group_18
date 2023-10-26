# Registration.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, bcrypt, User,Address,Payment_Method
registration_blueprint = Blueprint('registration', __name__)
@registration_blueprint.route("/registration", methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone number']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        address = request.form['address']
        payment_method = request.form['payment method']
        with open('Sign_Up_Pages\Registration\Registration.txt', 'a') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Password: {password}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Payment Method: {payment_method}\n")
        user = User(name=name,email=email,phone_number=phone_number,password=hashed_password)
        address_col = Address(address=address,default=True)
        payment_method_col = Payment_Method(card_num=payment_method,default=True)
        user.addresses.append(address_col)
        user.payment_methods.add(payment_method_col)
        try:
            db.session.add(user)
            db.session.commit()
            flash('User registered.','success')
            return redirect(url_for('homepage.homepage'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error registering user', 'danger')
            return render_template('registration.html')
    return render_template('registration.html')



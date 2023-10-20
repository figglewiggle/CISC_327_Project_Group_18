#Registration.py
from flask import Blueprint, render_template, request
registration_blueprint = Blueprint('registration', __name__)
@registration_blueprint.rout("/registration", methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone number']
        password = request.form['password']
        address = request.form['address']
        payment_method = request.form['payment method (card number)']
        with open('CISC_327_Project\Sign_Up_Pages\Registration\Registration.txt', 'w') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Password: {password}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Payment Method: {payment_method}\n")
        return render_template('registration.html')
    return render_template('registration.html')



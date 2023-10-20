# Login.py
from flask import Blueprint, render_template, request
login_blueprint = Blueprint('login',__name__)
@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        with open('CISC_327_Project\Sign_Up_Pages\Login\Login.txt','w') as file:
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
        return render_template('login.html')
    return render_template('login.html')

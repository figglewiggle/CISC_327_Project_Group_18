# Login.py
from flask import Blueprint, render_template, request, url_for, redirect, flash
from models import User, bcrypt
login_blueprint = Blueprint('login',__name__)
@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        with open('Sign_Up_Pages\Login\Login.txt','w') as file:
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
        try:
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                return redirect(url_for('homepage.homepage'))
            flash('Invalid email or password, try again.','danger')
            return render_template('login.html')
        except Exception:
            flash(f'User not found','danger')
            return render_template('login.html')
    return render_template('login.html')


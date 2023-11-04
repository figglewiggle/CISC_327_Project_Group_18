# Login.py
from flask import Blueprint, render_template, request, url_for, redirect, flash
from models import User, bcrypt, db, Item
from flask_login import login_user
login_blueprint = Blueprint('login',__name__)
@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    items = Item.query.all()
    if items:
        for item in items:
            item.in_cart = False # reset cart items when you login
        db.session.commit()
    if request.method=='POST': # if form has been submitted
        email = request.form['email']
        password = request.form['password']
        with open('Sign_Up_Pages\Login\Login.txt','a') as file: # write the email and password for testing purposes
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n")
        try: 
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password): # verifies that password inputted matches the secured password for the account
                login_user(user)
                return redirect(url_for('homepage.homepage'))
            flash('Invalid email or password, try again.','danger')
            return render_template('login.html')
        except Exception: # throws error if user is not found
            flash(f'User not found','danger')
            return render_template('login.html')
    return render_template('login.html')


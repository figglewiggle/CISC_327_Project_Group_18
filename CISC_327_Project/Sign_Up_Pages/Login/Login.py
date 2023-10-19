# Login.py
from Objects import User
from flask import Blueprint, render_template, request
login_blueprint = Blueprint('login',__name__)
@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username,"some@gmail.com",14167659069,password,["145 Division Street"],4525385498719082)
        return render_template('login.html')
    return render_template('login.html')
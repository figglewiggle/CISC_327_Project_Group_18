from flask import Blueprint, redirect, url_for, session
from flask_login import logout_user, login_required
logout_blueprint = Blueprint('logout',__name__)
@logout_blueprint.route('/logout',methods=['GET', 'POST'])
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('login.login'))

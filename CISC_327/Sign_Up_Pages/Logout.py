from flask import Blueprint, redirect, url_for, session
from models import db, Item
from flask_login import logout_user, login_required
logout_blueprint = Blueprint('logout',__name__)
@logout_blueprint.route('/logout',methods=['GET', 'POST'])
@login_required # You have to login first to logout
def logout():
    items = Item.query.all()
    if items:
        for item in items:
            item.in_cart = False # Get rid of the cart items once you logout
        db.session.commit()
    session.clear()
    logout_user()
    return redirect(url_for('login.login'))

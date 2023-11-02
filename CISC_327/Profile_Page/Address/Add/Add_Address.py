from flask import Blueprint, request, redirect, url_for
from flask_login import current_user
from models import db, Address
add_address_blueprint = Blueprint('add_address',__name__)
@add_address_blueprint.route('/add_address',methods=['GET', 'POST'])
def add_address():
    address_name = request.form.get('address')
    address = Address(address=address_name, default=False)
    current_user.addresses.append(address)
    db.session.add(address)
    db.session.commit()
    return redirect(url_for('profile.profile'))
    
    
        
from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user
from models import db, Address
add_address_blueprint = Blueprint('add_address',__name__)
@add_address_blueprint.route('/add_address',methods=['GET', 'POST'])
def add_address():
    if request.method=='POST':
        address_name = request.form.get('address') 
        if address_name:
            address = Address(address=address_name, default=False)
            current_user.addresses.append(address)
            db.session.add(address)
            db.session.commit()
        else:
           flash(f'Invalid input','danger') 
        return redirect(url_for('profile.profile'))
    
    
        
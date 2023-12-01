from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user
from ....models import db, Address
import re
add_address_blueprint = Blueprint('add_address',__name__)
@add_address_blueprint.route('/add_address',methods=['GET', 'POST'])
def add_address():
    if request.method=='POST':
        address_name = request.form.get('address') 
        address_pattern = re.compile(r'^[a-zA-Z0-9 ]+$')
        if not address_name or not address_pattern.match(address_name) or len(address_name)>50:
            flash('Invalid address format. Please use a valid address.', 'danger')
        else:
            address = Address(address=address_name, default=False)
            current_user.addresses.append(address)
            db.session.add(address)
            db.session.commit() 
        return redirect(url_for('profile.profile'))
    
    
        
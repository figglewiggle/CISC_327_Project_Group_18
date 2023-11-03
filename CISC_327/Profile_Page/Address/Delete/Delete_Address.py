from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user
from models import db, Address
delete_address_blueprint = Blueprint('delete_address',__name__)
@delete_address_blueprint.route('/delete_address', methods=['POST'])
def delete_address():
    address_id = request.form.get('address_id')
    address = Address.query.get(address_id)
    if address.user_id == current_user.id and len(current_user.addresses.all())>1:
        db.session.delete(address)
        db.session.commit()
        flash('Address deleted successfully!', 'success')
    else:
        flash('Unauthorized', 'danger')
    return redirect(url_for('profile.profile'))

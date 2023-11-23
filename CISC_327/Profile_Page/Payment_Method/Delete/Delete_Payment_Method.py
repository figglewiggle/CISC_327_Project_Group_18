from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user
from ....models import db, Payment_Method
delete_payment_blueprint = Blueprint('delete_payment',__name__)
@delete_payment_blueprint.route('/delete_payment', methods=['POST'])
def delete_payment():
    payment_id = request.form.get('payment_id') # get id of payment method row
    payment_method = Payment_Method.query.get(payment_id) 
    if payment_method.user_id == current_user.id and len(current_user.payment_methods.all())>1: # only delete payment method if there's more than one
        db.session.delete(payment_method)
        db.session.commit()
        flash('Payment Method deleted successfully!', 'success')
    else:
        flash('Unauthorized', 'danger')
    return redirect(url_for('profile.profile'))

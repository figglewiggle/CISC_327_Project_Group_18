from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user
from ....models import db, Payment_Method
import re
add_payment_blueprint = Blueprint('add_payment',__name__)
@add_payment_blueprint.route('/add_payment',methods=['GET', 'POST'])
def add_payment():
    if request.method == 'POST': # if form is submitted
        card_num = request.form.get('card_num')
        payment_pattern = re.compile(r'^[0-9]+$')
        if not card_num or not payment_pattern.match(card_num) or len(card_num)!=16:
            flash('Invalid payment method format. Please use a valid payment method.', 'danger')
        else:
            payment_method = Payment_Method(card_num=card_num, default=False) # add payment method
            current_user.payment_methods.append(payment_method) # associate with current user
            db.session.add(payment_method)
            db.session.commit()
        return redirect(url_for('profile.profile'))
    
    
        

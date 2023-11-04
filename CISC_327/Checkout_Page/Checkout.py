from flask import Blueprint, render_template, request, flash, session
from models import Item, Restaurant
from flask_login import current_user
import Cart_Page.Subtotal.Subtotal as Subtotal
checkout_blueprint = Blueprint('checkout',__name__)
@checkout_blueprint.route("/checkout/<restaurant_id>", methods=['GET','POST'])
def checkout(restaurant_id):
    subtotal = Subtotal.subtotal()
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        flash(f'Restaurant not found','danger')
    cart_items = Item.query.filter(Item.in_cart==True).all()
    if current_user.is_authenticated:
        checkout_pm = current_user.payment_methods.filter_by(default=True).first()
        checkout_address = current_user.addresses.filter_by(default=True).first()
        if request.method=="POST":
            form_data = request.form.items()
            for key,value in form_data:
                if key == "change_address":
                    session['change_address'] = request.form['change_address']
                    new_a = request.form['change_address']
                    checkout_address = current_user.addresses.filter_by(address=new_a).first()
                    pm_data = session.get('change_pm')  
                    if pm_data:
                        checkout_pm = current_user.payment_methods.filter_by(card_num=pm_data).first()                
                else:
                    session['change_pm'] = request.form['change_pm']
                    new_pm = request.form['change_pm']
                    checkout_pm = current_user.payment_methods.filter_by(card_num=new_pm).first()
                    address_data = session.get('change_address')  
                    if address_data:
                        checkout_address = current_user.addresses.filter_by(address=address_data).first()
        
        name = current_user.name
        email = current_user.email
        phone_number = current_user.phone_number
        
        all_addresses = current_user.addresses.all()
        all_pm = current_user.payment_methods.all()

    tax = subtotal*0.14
    total = tax + subtotal
    tip = session.get('tip')
    if tip:
        tip_dec = int(tip)/100
        t = total * tip_dec
        tot = total + t
        total = round(tot,3)
  
    return render_template("checkout.html", restaurant=restaurant,cart_items=cart_items,subtotal=subtotal,
                           total=total,tax=tax,name=name,email=email,phone_number=phone_number,address=checkout_address,all_addresses=all_addresses,all_pm=all_pm,payment_method=checkout_pm)
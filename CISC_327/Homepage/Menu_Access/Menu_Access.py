# Menu_Access.py
from flask import Blueprint, render_template, flash
from ...models import Restaurant
menu_blueprint = Blueprint('menu',__name__)
@menu_blueprint.route("/menu/<restaurant_id>", methods=['GET','POST'])
def menu(restaurant_id): # access menu of a given restaurant clicked on
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant: # error check if restaurant no found
        flash(f'Restaurant not found','danger')
        return render_template("homepage.html")
    items = restaurant.item_list 
    return render_template("menupage.html", restaurant_id=restaurant_id, restaurant_name = restaurant.name, 
                           restaurant_address=restaurant.address, restaurant_phone_number = restaurant.phone_number,
                           restaurant_cuisine = restaurant.cuisine, items=items) # display everything about the restaurant on the menupage
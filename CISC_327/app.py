# Restaurant_App
# This is a food delivery app that lets a user login and order from their favourite restaurants
# and get their food straight at their door
# this is run on a website: https://restaurant-group-18-ab6d36ffaa44.herokuapp.com/
from flask import Flask, url_for, redirect
from Seed_Heroku_DB import seed_heroku_db
from Sign_Up_Pages.Login.Login import login_blueprint
from Sign_Up_Pages.Registration.Registration import registration_blueprint
from Homepage.Homepage import homepage_blueprint
from Profile_Page.Profile import profile_blueprint
from Cart_Page.Cartpage import cartpage_blueprint
from Homepage.Menu_Access.Menu_Access import menu_blueprint
from Sign_Up_Pages.Logout import logout_blueprint
from Homepage.Search.Text_Search.Text_Search import text_search_blueprint
from Checkout_Page.Checkout import checkout_blueprint
from Checkout_Page.Tips.Tips import tips_blueprint
from Cart_Page.Add.Add_To_Cart import add_to_cart_blueprint
from Cart_Page.Delete.Delete_From_Cart import delete_from_cart_blueprint
from Homepage.Search.Filter_Search.Filter_Search import filter_search_blueprint
from Profile_Page.Address.Add.Add_Address import add_address_blueprint
from Profile_Page.Address.Delete.Delete_Address import delete_address_blueprint
from Profile_Page.Edit_Password.Edit_Password import edit_password_blueprint
from Profile_Page.Edit_Phone_Number.Edit_Phone_Number import edit_phone_blueprint
from Profile_Page.Payment_Method.Add.Add_Payment_Method import add_payment_blueprint
from Profile_Page.Payment_Method.Delete.Delete_Payment_Method import delete_payment_blueprint
from Tracking_Page.Tracking import tracking_blueprint
from models import db, bcrypt, User, Restaurant, Item
from flask_migrate import Migrate, migrate
import os
import click
from flask_login import LoginManager
app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL','sqlite:///site.db').replace("postgres://", "postgresql://")
if os.environ.get('FLASK_ENV') == 'testing':
    # Testing configuration
    app.config.from_object('tests.config_test.TestConfig')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = 'the random string'
login_manager = LoginManager()
login_manager.login_view = "login.login"
migrate = Migrate(app, db)
login_manager.init_app(app)
db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)

@app.cli.command("delete-user") # deletes user rows to prevent over saturation of the database
@click.argument("user_id")
def delete_user_command(user_id):
    """Deletes a user with the given user_id and all related rows, to clear test cases."""
    with app.app_context():
        user = User.query.get(user_id)
        if not user:
            click.echo(f"User with ID {user_id} not found.")
            return
        db.session.delete(user)
        db.session.commit()
        click.echo(f"User with ID {user_id} and related posts deleted.")
        
@app.cli.command("display-user") # displays user rows for testing purposes (guides deletion)
@click.argument("user_name")
def display_user_command(user_name):
    """Displays a user with the given user_id, to help with testing"""
    with app.app_context():
        user= User.query.get(user_name)
        if not user:
            click.echo(f"User with ID {user_name} not found.")
            return
        print(user.__repr__())

@app.cli.command("add-restaurant") # adds restaurant rows for testing purposes
def add_restaurant_command():
    with app.app_context():
        name = input("Enter Restaurant Name: ")
        phone_number = input("Enter Restaurant Phone Number:")
        address = input("Enter Address: ")
        cuisine = input("Enter Cuisine Type: ")
        restaurant= Restaurant(name=name, phone_number=phone_number, address=address, cuisine=cuisine)
        db.session.add(restaurant)
        db.session.commit()

@app.cli.command("add-item") # adds item rows for testing purposes (item functionalities)
@click.argument("restaurant_id")
def add_item_command(restaurant_id):
    with app.app_context():
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            click.echo(f"Restaurant with ID {restaurant_id} not found.")
            return
        name = input("Enter Name: ")
        description = input("Enter Description: ")
        price = input("Enter Price: ")
        item = Item(name=name, description=description, price=price, in_cart=False)
        restaurant.item_list.append(item)
        db.session.add(item)
        db.session.commit()

@app.cli.command("display-restaurant") # display restaurant info for testing purposes (guides deleting and adding)
@click.argument("restaurant_id")
def display_restaurant_command(restaurant_id):
    with app.app_context():
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            click.echo(f"Restaurant with ID {restaurant_id} not found.")
            return
        print(restaurant.__repr__())
        
@app.cli.command("delete-restaurant") # deletes restaurant row in the restaurant table, for testing purposes
@click.argument("restaurant_id")
def delete_restaurant_command(restaurant_id):
    """Deletes a user with the given user_id and all related rows, to clear test cases."""
    with app.app_context():
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            click.echo(f"Restaurant with ID {restaurant_id} not found.")
            return
        db.session.delete(restaurant)
        db.session.commit()
        click.echo(f"User with ID {restaurant_id} and related posts deleted.")

@app.cli.command("seed_heroku")
def seed_heroku_command():
    with app.app_context():
        seed_heroku_db()
    

# @app.cli.command("add-to-cart") 
# @click.argument("item_id")
# def add_to_cart_command(item_id):
#     with app.app_context():
#         item = Item.query.get(item_id)
#         if not item:
#             click.echo(f"Item with ID {item_id} not found.")
#             return
#         Item.query.filter(Item.id==item_id).update({Item.in_cart: True})
#         db.session.commit()

# helper function for flask-login to get current user for a given session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# redirect root route to login route, so that the first thing the user sees is a login page
@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('login.login'))

# register blueprints to the app so they render properly
app.register_blueprint(login_blueprint)
app.register_blueprint(registration_blueprint)
app.register_blueprint(homepage_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(cartpage_blueprint)
app.register_blueprint(menu_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(text_search_blueprint)
app.register_blueprint(checkout_blueprint)
app.register_blueprint(tips_blueprint)
app.register_blueprint(add_to_cart_blueprint)
app.register_blueprint(delete_from_cart_blueprint)
app.register_blueprint(filter_search_blueprint)
app.register_blueprint(add_address_blueprint)
app.register_blueprint(delete_address_blueprint)
app.register_blueprint(edit_password_blueprint)
app.register_blueprint(edit_phone_blueprint)
app.register_blueprint(add_payment_blueprint)
app.register_blueprint(delete_payment_blueprint)
app.register_blueprint(tracking_blueprint)

# run the app
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
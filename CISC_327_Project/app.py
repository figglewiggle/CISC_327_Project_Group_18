from flask import Flask, url_for, redirect
from Sign_Up_Pages.Login.Login import login_blueprint
from Sign_Up_Pages.Registration.Registration import registration_blueprint
from Homepage.Homepage import homepage_blueprint
from Profile_Page.Profile import profile_blueprint
from Cart_Page.Cartpage import cartpage_blueprint
from Homepage.Menu_Access.Menu_Access import menu_blueprint
from models import db, bcrypt, User
from flask_migrate import Migrate, migrate
import os
import click
from flask_login import LoginManager
app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL or 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'the random string'
login_manager = LoginManager()
login_manager.login_view = "login.login"
login_manager.init_app(app)
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)

@app.cli.command("delete-user")
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
        
@app.cli.command("display-user")
@click.argument("user_id")
def display_user_command(user_id):
    """Displays a user with the given user_id, to help with testing"""
    with app.app_context():
        user= User.query.get(user_id)
        if not user:
            click.echo(f"User with ID {user_id} not found.")
            return
        print(user.__repr__())
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('login.login'))

app.register_blueprint(login_blueprint)
app.register_blueprint(registration_blueprint)
app.register_blueprint(homepage_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(cartpage_blueprint)
app.register_blueprint(menu_blueprint)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port, debug=True, threaded=True)
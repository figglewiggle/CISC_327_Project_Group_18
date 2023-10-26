from flask import Flask, url_for, redirect
from Sign_Up_Pages.Login.Login import login_blueprint
from Sign_Up_Pages.Registration.Registration import registration_blueprint
from Homepage.Homepage import homepage_blueprint
from Profile_Page.Profile import profile_blueprint
from Cart_Page.Cartpage import cartpage_blueprint
from Homepage.Menu_Access.Menu_Access import menu_blueprint
from models import db, bcrypt
from flask_migrate import Migrate, migrate
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'the random string'
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
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
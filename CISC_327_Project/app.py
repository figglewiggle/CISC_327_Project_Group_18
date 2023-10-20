from flask import Flask, render_template, request, url_for, redirect
from Sign_Up_Pages.Login.Login import login_blueprint
from Sign_Up_Pages.Registration.Registration import registration_blueprint
from Homepage.Homepage import homepage_blueprint
from Profile_Page.Profile import profile_blueprint
from Cart_Page.Cartpage import cartpage_blueprint
from Homepage.Menu_Access.Menu_Access import menu_blueprint
import os
app = Flask(__name__)

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host="127.0.0.0", port=port, debug=True, threaded=True)
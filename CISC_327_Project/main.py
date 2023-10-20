from flask import Flask, render_template, request, url_for, redirect
from Sign_Up_Pages.Login.Login import login_blueprint
from Sign_Up_Pages.Registration.Registration import registration_blueprint
from Homepage.Homepage import homepage_blueprint
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('login.login'))
app.register_blueprint(login_blueprint)
app.register_blueprint(registration_blueprint)
app.register_blueprint(homepage_blueprint)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
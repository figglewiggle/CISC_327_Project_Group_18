from flask import Flask, render_template, request, url_for, redirect
from Sign_Up_Pages.Login.Login import login_blueprint
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('login'))
app.register_blueprint(login_blueprint)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
# Text_Search.py
from flask import Blueprint, render_template
from flask_login import current_user, login_required
text_search_blueprint = Blueprint('text_search',__name__)
@text_search_blueprint.route('/text_search/', methods=['GET','POST'])
def text_search():
    return render_template('homepage.html')


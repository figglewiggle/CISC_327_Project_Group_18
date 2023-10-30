# Text_Search.py
from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from models import Restaurant
text_search_blueprint = Blueprint('text_search',__name__)
@text_search_blueprint.route('/search/', methods=['GET','POST'])
def text_search():
    query = request.args.get('q', '')  # Get the search input
    restaurants = Restaurant.query.filter(Restaurant.name.like(f"%{query}%")).all()
    return render_template('homepage.html', restaurants=restaurants)


# Filter_Search.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from models import Restaurant
from flask_login import current_user
filter_search_blueprint = Blueprint('filter_search',__name__)

@filter_search_blueprint.route('/get_cuisines', methods=['GET','POST'])
def get_cuisines():
    restaurants = Restaurant.query.filter_by().all()
    cuisine_list = set()
    for restaurant in restaurants:
        cuisine_list.add(restaurant.cuisine)
    print(cuisine_list)
    return render_template('filter_search.html',cuisine_list=cuisine_list)

@filter_search_blueprint.route('/filter_search',methods=['GET','POST'])
def filter_search():
    cuisine = request.form.get('cuisine')
    session['selected_cuisine'] = cuisine
    return redirect(url_for('homepage.homepage'))
    
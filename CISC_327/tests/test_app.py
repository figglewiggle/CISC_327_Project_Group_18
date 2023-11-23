# test_app.py
# to r7 first).
# to record the output: pytest > test_results.txt on the command line or pip install pytest-html, and then un the test on the command line, first type: FLASK_ENV=testing in the terminal on vscode (navigate to CISC_32pytest --html=report.html
import pytest
from app import app as flask_app
from flask import url_for
<<<<<<< HEAD
from models import Item
@pytest.fixture
=======
from flask_migrate import upgrade
from models import Item, User
@pytest.fixture(scope='module')
>>>>>>> afb03e711eeba6c9d4b59ac1811d71c0d823b10b
def app():
    flask_app.config.from_object('tests.config_test.TestConfig')
    print("Database URI (Test):", flask_app.config['SQLALCHEMY_DATABASE_URI'])  # Debugging line
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 302

<<<<<<< HEAD
# test_user_authentication.py
from flask import Flask
from flask.testing import FlaskClient
from app import app as flask_app
from models import db, User

def test_user_registration():
    client = flask_app.test_client()

=======
def test_user_registration(client):
>>>>>>> afb03e711eeba6c9d4b59ac1811d71c0d823b10b
    # User Registration Test
    response = client.post('/registration', data=dict(
        name='Test User',
        email='test@example.com',
        phone_number='1234567890',
        password='testpassword',
        address='Test Address',
        payment_method='1234567890123456'
    ), follow_redirects=True)
    
    print('Status Code:', response.status_code)
    print('Response:', response.data.decode('utf-8'))  # Assuming response

    # Assert the registration result
    assert response.status_code == 200  # Check if the registration is successful
    assert response.request.path == url_for('homepage.homepage'), "Did not redirect to the homepage"

    registered_user = User.query.filter_by(email='test@example.com').first()
    assert registered_user is not None  # Check if the user is registered in the database
    
    assert registered_user.addresses.first() is not None, "Address was not registered"
    assert registered_user.payment_methods.first() is not None, "Payment method was not registered"

def test_user_login():
    client = flask_app.test_client()

def test_user_login(client):
    # User Login Test
    response = client.post('/login', data=dict(
        email='test@example.com',
        password='testpassword'
    ), follow_redirects=True)

    # Assert the login result
    assert response.status_code == 200  # Check if the login is successful

    # You can add additional assertions based on your application's behavior after successful login

def test_menu_access(client):
    response = client.post('/menu/1', follow_redirects = True)
    assert response.status_code == 200, f"Did not get the expected status code"  

def test_add_to_cart(client):
    response = client.post('/add_to_cart/1/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Chicken Alfredo Pasta added to cart!' in response.data
def test_add_to_cart_valid(client):
    response = client.post('/add_to_cart/1/1', follow_redirects=True) 
    item = Item.query.get(1)
    assert item.in_cart is True, f"Item was not added to cart" # Check to make sure that item is in the cart
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'Chicken Alfredo Pasta added to cart!' in response.data, f"Item was not added to cart so the flash message was not displayed" # Checks for the flash message in the html 
    print('Add To Cart Test - Status Code: ', response.status_code)
    print('Add To Cart Test - Response: ', response.data.decode('utf-8'))

def test_add_to_cart_invalid(client):
    response = client.post('/add_to_cart/0/0', follow_redirects=True) 
    item = Item.query.get(1)
    assert item.in_cart is True, f"Item was not added to cart" # Check to make sure that item is in the cart
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'Chicken Alfredo Pasta added to cart!' in response.data, f"Item was not added to cart so the flash message was not displayed" # Checks for the flash message in the html 
    print('Add To Cart Test - Status Code: ', response.status_code)
    print('Add To Cart Test - Response: ', response.data.decode('utf-8'))

def test_delete_from_cart_valid(client):
    item = Item.query.get(1)
    item.in_cart = True # Put the item in the cart first
    response = client.post('/delete_from_cart/1/1', follow_redirects=True)
    assert response.status_code == 200
    assert item.in_cart is False

def test_subtotal(client):
    response = client.get('/cartpage/1', follow_redirects=True)
    assert response.status_code == 200
    print('Delete From Cart Test - Status Code: ', response.status_code)
    print('Delete From Cart Test - Response: ', response.data.decode('utf-8'))
    assert response.status_code == 200, f"Did not get the expected status code"
    assert item.in_cart is False, f"The item was not removed from the cart" # Check that is has been removed from cart

def test_delete_from_cart_invalid(client):
    item = Item.query.get(1)
    item.in_cart = True # Put the item in the cart first
    response = client.post('/delete_from_cart/0/1', follow_redirects=True)
    print('Delete From Cart Test - Status Code: ', response.status_code)
    print('Delete From Cart Test - Response: ', response.data.decode('utf-8'))
    assert response.status_code == 200, f"Did not get the expected status code"
    assert item.in_cart is False, f"The item was not removed from the cart" # Check that is has been removed from cart


def test_subtotal_valid(client):
    item = Item.query.get(1)
    item.in_cart = True # Put an item in the cart so that the cart page can be opened
    response = client.get('/cartpage/1', follow_redirects=True)
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'$15' in response.data, f"Did not get the expected subtotal " # Check that the price of the item is listed
    print('Subtotal Test - Status Code:', response.status_code)
    print('Subtotal Test - Response: ', response.data.decode())

def test_subtotal_invalid(client):
    item = Item.query.get(1)
    item.in_cart = True # Put an item in the cart so that the cart page can be opened
    response = client.get('/cartpage/0', follow_redirects=True)
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'$15' in response.data, f"Did not get the expected subtotal " # Check that the price of the item is listed
    print('Subtotal Test - Status Code:', response.status_code)
    print('Subtotal Test - Response: ', response.data.decode())

def test_search_valid(client):
    # Makes request to search function with the specified query
    response = client.get(f'/search/?q=Jack Astor\'s', follow_redirects=True)
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'Jack Astor' in response.data, f"The expected search result was not displayed"
    print('Search Bar Test - Status Code:', response.status_code)
    print('Search Bar Test - Response: ', response.data.decode())

def test_search_invalid(client):
    # Makes request to search function with the specified query
    response = client.get(f'/search/?q=Jack Ator\'s', follow_redirects=True)
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'Jack Astor' in response.data, f"The expected search result was not displayed"
    print('Search Bar Test - Status Code:', response.status_code)
    print('Search Bar Test - Response: ', response.data.decode())


    
    

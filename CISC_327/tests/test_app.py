# test_app.py
# to r7 first).
# to record the output: pytest > test_results.txt on the command line or pip install pytest-html, and then un the test on the command line, first type: FLASK_ENV=testing in the terminal on vscode (navigate to CISC_32pytest --html=report.html
import pytest
from app import app as flask_app
from flask import url_for
from models import Item
@pytest.fixture
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

# test_user_authentication.py
from flask import Flask
from flask.testing import FlaskClient
from app import app as flask_app
from models import db, User

def test_user_registration():
    client = flask_app.test_client()

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
    assert response.status_code == 200  

def test_add_to_cart(client):
    response = client.post('/add_to_cart/1/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Chicken Alfredo Pasta added to cart!' in response.data

def test_delete_from_cart(client):
    item = Item.query.get(1)
    item.in_cart = True
    response = client.post('/delete_from_cart/1/1', follow_redirects=True)
    assert response.status_code == 200
    assert item.in_cart is False



def test_subtotal(client):
    response = client.get('/cartpage/1', follow_redirects=True)
    
    assert response.status_code == 200



    
    

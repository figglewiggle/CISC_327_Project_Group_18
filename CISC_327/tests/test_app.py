from flask import url_for
from ..models import Item, User, bcrypt

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 302

def test_user_registration(client):
    # User Registration Test
    response = client.post('/registration', data=dict(
        name='Test User',
        email='tipi@gmail.com',
        phone_number='1234567890',
        password='testpassword',
        address='Test Address',
        payment_method='1234567890123456'
    ), follow_redirects=True)
    
    print('Status Code:', response.status_code)
    print('Response:', response.data.decode('utf-8'))  # Assuming response

    # Assert the registration result
    assert response.status_code == 200  # Check if the registration is successful
    assert 'login' in response.request.path, "Did not redirect to the login page"

    registered_user = User.query.filter_by(email='tipi@gmail.com').first()
    assert registered_user is not None  # Check if the user is registered in the database
    
    assert registered_user.addresses.first() is not None, "Address was not registered"
    assert registered_user.payment_methods.first() is not None, "Payment method was not registered"

def test_user_login(client):
    # User Login Test
    response = client.post('/login', data=dict(
        email='tipi@gmail.com',
        password='testpassword'
    ), follow_redirects=True)

    # Assert the login result
    assert response.status_code == 200  # Check if the login is successful

def test_homepage_2(client):
    response = client.get('/homepage', follow_redirects = True)
    assert response.status_code == 200, f"Did not get the expected status code"

def test_profile_page(client):
    response = client.get('/profile', follow_redirects = True)
    assert response.status_code == 200, f"Did not get the expected status code"

def test_add_address(client):
    new_address = '123 Test Street'
    response = client.post('/add_address', data=dict(
        address=new_address
    ), follow_redirects=True)
    assert response.status_code == 200
    assert 'profile' in response.request.path, "Did not redirect to the profile page"
    current_user = User.query.filter_by(email='tipi@gmail.com').first()
    added_address = current_user.addresses.filter_by(address=new_address).first()
    assert added_address is not None, "Address was not added to the user's addresses"
    assert added_address.default is False, "New address should not be set as default"
    with client.session_transaction() as session:
        session.clear()

def test_delete_address(client):
    current_user = User.query.filter_by(email='tipi@gmail.com').first()
    added_address = current_user.addresses.filter_by(address='123 Test Street').first()
    address_id = added_address.id
    response_delete_address = client.post('/delete_address', data=dict(
        address_id=address_id
    ), follow_redirects=True)
    assert response_delete_address.status_code == 200
    assert 'profile' in response_delete_address.request.path, "Did not redirect to the profile page"


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
    assert item.quantity==2, f"Item quantity not updated"
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'Chicken Alfredo Pasta added to cart!' in response.data, f"Item was not added to cart so the flash message was not displayed" # Checks for the flash message in the html 
    print('Add To Cart Test - Status Code: ', response.status_code)
    print('Add To Cart Test - Response: ', response.data.decode('utf-8'))

def test_add_to_cart_invalid(client):
    response = client.post('/add_to_cart/0/0', follow_redirects=True) 
    item = Item.query.get(1)
    assert item.in_cart is True, f"Item was not added to cart" # Check to make sure that item is in the cart
    assert item.quantity==1, f"Item quantity not updated"
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'Chicken Alfredo Pasta added to cart!' in response.data, f"Item was not added to cart so the flash message was not displayed" # Checks for the flash message in the html 
    print('Add To Cart Test - Status Code: ', response.status_code)
    print('Add To Cart Test - Response: ', response.data.decode('utf-8'))

def test_delete_from_cart_valid(client):
    item = Item.query.get(1)
    item.in_cart = True # Put the item in the cart first
    item.quantity = 1
    response = client.post('/delete_from_cart/1/1', follow_redirects=True)
    print('Delete From Cart Test - Status Code: ', response.status_code)
    print('Delete From Cart Test - Response: ', response.data.decode('utf-8'))
    assert response.status_code == 200, f"Did not get the expected status code"
    assert item.in_cart is False, f"The item was not removed from the cart" # Check that is has been removed from cart
    assert item.quantity==0, f"Item was not reset"

def test_subtotal(client):
    response = client.get('/cartpage/1', follow_redirects=True)
    assert response.status_code == 200
    

def test_delete_from_cart_invalid(client):
    item = Item.query.get(1)
    item.in_cart = True # Put the item in the cart first
    item.quantity = 1
    response = client.post('/delete_from_cart/0/1', follow_redirects=True)
    print('Delete From Cart Test - Status Code: ', response.status_code)
    print('Delete From Cart Test - Response: ', response.data.decode('utf-8'))
    assert response.status_code == 200, f"Did not get the expected status code"
    assert item.in_cart is False, f"The item was not removed from the cart" # Check that is has been removed from cart
    assert item.quantity==0, f"Item was not reset" 


def test_subtotal_valid(client):
    item = Item.query.get(1)
    item.in_cart = True # Put an item in the cart so that the cart page can be opened
    item.quantity = 1
    response = client.get('/cartpage/1', follow_redirects=True)
    assert response.status_code == 200, f"Did not get the expected status code"
    assert b'$15' in response.data, f"Did not get the expected subtotal " # Check that the price of the item is listed
    print('Subtotal Test - Status Code:', response.status_code)
    print('Subtotal Test - Response: ', response.data.decode())

def test_subtotal_invalid(client):
    item = Item.query.get(1)
    item.in_cart = True # Put an item in the cart so that the cart page can be opened
    item.quantity = 1
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
    assert b'Jack Astor\'s' in response.data, f"The expected search result was not displayed"
    print('Search Bar Test - Status Code:', response.status_code)
    print('Search Bar Test - Response: ', response.data.decode())


    
def test_add_tip(client):
    item = Item.query.get(1)
    response = client.post('/tips/1', data=dict(
        tip='10'
    ), follow_redirects=True)
    assert response.status_code == 200
    with client.session_transaction() as session:
        assert session.get('tip') == '10'
    assert b'Tip: 10%' in response.data, "Tip percentage not displayed on the checkout page"
    with client.session_transaction() as session:
        session.clear()

def test_cart_page(client):
    response = client.post('/cartpage/1', follow_redirects = True)
    assert response.status_code == 200, f"Did not get the expected status code"  

def test_checkout_page(client):
    response = client.post('/checkout/1', follow_redirects = True)
    assert response.status_code == 200, f"Did not get the expected status code"

def test_edit_password(client):
    response = client.post('/edit_password', data={'new_password': 'newpassword'}, follow_redirects=True)
    hashed = bcrypt.generate_password_hash('newpassword').decode('utf-8')
    user = User.query.filter_by(email='tipi@gmail.com').first()
    assert response.status_code == 200, f"Did not get the expected status code"  
    assert user.password == hashed 

def test_add_payment(client):
    response = client.post('/add_payment', data={'card_num':'1234567890123455'}, follow_redirects=True)
    assert response.status_code == 200, f"Did not get the expected status code" 
    assert b'1234567890123455'in response.data, f"The expected search result was not displayed"
    print('Add Payment Test - Status Code:', response.status_code)
    print('Add Payment Test - Response: ', response.data.decode())
def test_logout(client):
    response = client.post('/registration', data=dict(
        name='Test User',
        email='tipi@gmail.com',
        phone_number='1234567890',
        password='testpassword',
        address='Test Address',
        payment_method='1234567890123456'
    ), follow_redirects=True)
    response = client.post('/login', data=dict(
        email='tipi@gmail.com',
        password='testpassword'
    ), follow_redirects=True)
    response = client.get(f'/logout', follow_redirects=True)
    assert response.status_code == 200, f"Did not get the expected status code"
    assert 'login' in response.request.path, "Did not redirect to the login page"




def test_delete_payment(client):
    response = client.post('/add_payment', data={'card_num':'1234567890123455'}, follow_redirects=True)
    response = client.post('/delete_payment', data={'payment_id':'1'}, follow_redirects=True)
    assert response.status_code == 200, f"Did not get the expected status code" 
    assert b'1234567890123455' not in response.data, f"The expected search result was not displayed"
    print('Delete Payment Test - Status Code:', response.status_code)
    print('Delete Payment Test - Response: ', response.data.decode('utf-8'))


    

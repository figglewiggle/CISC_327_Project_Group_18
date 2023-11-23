#test_whitebox.py
from flask import url_for
from ..models import Item, User
from CISC_327.Profile_Page.Edit_Phone_Number import edit_phone

def test_filter_search_1(client):
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
    response = client.post('/filter_search', data={'cuisine':'American'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Jack Astor' in response.data
    print('Test 1 HTML: ', response.data.decode('utf-8'))

def test_filter_search_2(client):
    response = client.post('/filter_search', data={'cuisine':'Vietnamese'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Pho Kingston' in response.data
    print('Test 2 HTML: ', response.data.decode('utf-8'))

def test_filter_search_3(client):
    response = client.post('/filter_search', data={}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Jack Astor' in response.data
    assert b'Pho Kingston' in response.data
    print('Test 3 HTML: ', response.data.decode('utf-8'))

def test_edit_phone_number(client):
    result = edit_phone()
    assert result == url_for('profile.profile')

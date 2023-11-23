#test_whitebox.py
from flask import url_for
from ..models import Item, User

def test_edit_phone_number(client):
    from Edit_Phone_Number import edit_phone
    result = edit_phone()
    assert result == url_for('profile.profile')

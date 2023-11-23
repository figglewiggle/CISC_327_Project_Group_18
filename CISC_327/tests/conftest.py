# conftest.py
# to r7 first).
# to record the output: pytest > test_results.txt on the command line or pip install pytest-html, and then un the test on the command line, first type: FLASK_ENV=testing in the terminal on vscode (navigate to CISC_32pytest --html=report.html
import pytest
from flask_migrate import upgrade
from ..app import create_app
from ..config import TestingConfig
from ..models import db, Restaurant, Item
@pytest.fixture(scope='session')
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        upgrade()
        populate_test_data()
        yield app
        db.session.remove()

def populate_test_data():
    item1 = Item(name="Chicken Alfredo Pasta", description="Ingredients: Grilled Chicken Strips, Alfredo Sauce, Penne", 
                 price=15, in_cart=False)
    item2 = Item(name="House Fries", description="Ingredients: Fried Potatoes", price=5, in_cart=False)
    db.session.add(item1)
    db.session.add(item2)
    restaurant1 = Restaurant(name="Jack Astor's", phone_number="4165738923", 
                             address="125 King Street", cuisine="American", item_list=[item1, item2])
    db.session.add(restaurant1)
    item3 = Item(name="Pho Dac Biet", 
                 description="Ingredients: Beef Broth, Chicken, Rice Noodles, Beef Balls, Brisket, Bean Sprouts",
                 price=15, in_cart=False)
    item4 = Item(name="Deep-Fried Rice Paper Spring Rolls",
                 description="Ingredients: Shrimp, Rice Paper, Onions, Mushrooms",
                 price=7, in_cart=False)
    db.session.add(item3)
    db.session.add(item4)
    restaurant2 = Restaurant(name="Pho Kingston", phone_number="6478923478", address="1289 Bath Road", cuisine="Vietnamese",
                             item_list=[item3, item4])
    db.session.add(restaurant2)
    db.session.commit()
    
@pytest.fixture
def client(app):
    return app.test_client()


        





    
    

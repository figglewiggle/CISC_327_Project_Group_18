from .models import db, Restaurant, Item

def seed_heroku_db():
    data = [
        {
            "restaurant": {
                "name": "Jack Astor's",
                "phone_number": "4165738923",
                "address": "125 King Street",
                "cuisine": "American"
            },
            "item_list": [
                {"name": "Chicken Alfredo Pasta", "description": "Ingredients: Grilled Chicken Strips, Alfredo Sauce, Penne", 
                 "price": 15, "in_cart": False},
                {"name": "House Fries", "description": "Ingredients: Fried Potatoes", "price": 5, "in_cart": False}
            ]  
        },
        {
            "restaurant": {
                "name": "Pho Kingston",
                "phone_number": "6478923478",
                "address": "1298 Bath Road",
                "cuisine": "Vietnamese"
            },
            "item_list": [
                {"name": "Pho Dac Biet", "description": "Ingredients: Beef Broth, Chicken, Rice Noodles, Beef Balls, Brisket, Bean Sprouts", 
                 "price": 15, "in_cart": False},
                {"name": "Deep-Fried Rice Paper Spring Rolls", "description": "Ingredients: Shrimp, Rice Paper, Onions, Mushrooms",
                 "price": 7, "in_cart": False}
            ]
        }
    ]
    for entry in data:
        restaurant = Restaurant(**entry["restaurant"]) # add restaurant entry to database
        db.session.add(restaurant)
        db.session.flush()  # Flush to get the restaurant's ID immediately
        for item_data in entry["item_list"]:
            item = Item(**item_data, restaurant_id=restaurant.id) # use restaurant id here
            db.session.add(item)
    db.session.commit()
    
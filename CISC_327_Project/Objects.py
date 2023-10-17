class User:
    def __init__ (self, name, email, phone_number, password,address):
    #DFKVHFBVVFKVFWJLVNWEFNFV
    # DSLKNLKVNLKNVFLEJNVFEQLVNE
# Objects.py
class Cart:
    def __init__ (self, item, subtotal):
        self.item = item
        self.subtotal = subtotal
    
    def add_to_cart(item):

class Restaurant:
    def __init__(self, name, phone_number, address, cuisine_list, item_list, favourites_list):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.cuisine_list = cuisine_list
        self.item_list = item_list
        self.favourites_list = favourites_list
    
    def remove_favourite(self, item):
        self.favourites_list.remove(item)
    
    def get_name(self):
        return self.name
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_address(self):
        return self.address
    
    def get_cuisine_list(self):
        return

class Item:
    def __init__ (self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    
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

class Item:
    def __init__ (self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    
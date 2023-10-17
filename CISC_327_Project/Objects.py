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
        return self.cuisine_list

class Item:
    def __init__ (self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
class User:
    def __init__ (self, name, email, phone_number, password, address_list, card_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.addresses = address_list
        self.payment_methods = card_list

    def AddAddress(self):
        address = input(str("Please enter the address you want to add:\n"))
        self.addresses.append(address)
    
    def DeleteAddress(self):
        print("\nHere are the list of addresses:\n")
        for i in range(len(self.addresses)):
            print(str(i+1) + ". " + self.addresses[i])
        address_index = input(int("Which address would you like to delete? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        while address_index not in range(1, len(self.addresses) + 1):
            print("\nInvalid input. Please enter an address index that is in the list.")
            address_index = input(int("Which address would you like to delete? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        self.addresses.pop(address_index)

    def EditAddress(self):
        print("\nHere are the list of addresses:\n")
        for i in range(len(self.addresses)):
            print(str(i+1) + ". " + self.addresses[i])
        address_index = input(int("Which address would you like to edit? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        while address_index not in range(1, len(self.addresses) + 1):
            print("\nInvalid input. Please enter an address index that is in the list.")
            address_index = input(int("Which address would you like to edit? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        address = input(str("Please enter the new address:\n"))
        self.addresses[address_index] = address

    def EditEmail(self):
        email = input(str("Please enter the new email:\n"))
        self.email = email
    
    def EditName(self):
        name = input(str("Please enter the new name:\n"))
        self.name = name     

    def EditPhoneNumber(self):
        phone_number = input(str("Please enter the new phone number:\n"))
        self.phone_number = phone_number

    def AddPaymentMethod(self):
        card_number = input(str("Please enter the card number you want to add:\n"))
        self.payment_methods.append(card_number)

    def DeletePaymentMethod(self):
        print("\nHere are the list of payment methods:\n")
        for i in range(len(self.payment_methods):
            print(str(i+1) + ". " + self.payment_methods[i])
        card_index = input(int("Which card would you like to delete? (1 - " + str(len(self.payment_methods) + 1) + ")\n"))
        while card_index not in range(1, len(self.payment_methods) + 1):
            print("\nInvalid input. Please enter a card index that is in the list.")
            card_index = input(int("Which card would you like to delete? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        self.payment_methods.pop(card_index)

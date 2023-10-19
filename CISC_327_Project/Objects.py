from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return "Index page"
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username,"some@gmail.com",14167659069,password,["145 Division Street"],4525385498719082)
        print("User {user.name} tried to login with password: {user.password}")
        return render_template('login.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
class Cart:
    def __init__ (self, item_list, subtotal):
        self.item_list = item_list
        self.subtotal = subtotal
    
    def get_item_list(self):
        return self.item_list

    def get_subtotal(self):
        return self.subtotal

    def add_to_cart(self, item):
        self.item_list.add(item)
    
    def remove_from_cart(self, item):
        self.item_list.remove(item)


class Restaurant:
    def __init__(self, name, phone_number, address, cuisine_list, item_list, favourites_list = []):
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

class Homepage:
    def __init__ (self,user_obj, restaurants_near):
        self.user_obj = user_obj
        self.restaurants_near = restaurants_near
    
    
class User:
    def __init__ (self, name, email, phone_number, password, address_list, card_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.addresses = address_list
        self.payment_methods = [card_number]
        
    def get_name(self):
        return self.name
    
    
    def get_email(self):
        return self.email
    
    
    def get_phone_number(self):
        return self.phone_number
    
    def add_address(self):
        address = input(str("Please enter the address you want to add:\n"))
        self.addresses.append(address)
    
    def delete_address(self):
        print("\nHere are the list of addresses:\n")
        for i in range(len(self.addresses)):
            print(str(i+1) + ". " + self.addresses[i])
        address_index = input(int("Which address would you like to delete? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        while address_index not in range(1, len(self.addresses) + 1):
            print("\nInvalid input. Please enter an address index that is in the list.")
            address_index = input(int("Which address would you like to delete? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        self.addresses.pop(address_index)
        
    def edit_address(self):
        print("\nHere are the list of addresses:\n")
        for i in range(len(self.addresses)):
            print(str(i+1) + ". " + self.addresses[i])
        address_index = input(int("Which address would you like to edit? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        while address_index not in range(1, len(self.addresses) + 1):
            print("\nInvalid input. Please enter an address index that is in the list.")
            address_index = input(int("Which address would you like to edit? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        address = input(str("Please enter the new address:\n"))
        self.addresses[address_index] = address
        
    def edit_email(self):
        email = input(str("Please enter the new email:\n"))
        self.email = email
        
    def edit_name(self):
        name = input(str("Please enter the new name:\n"))
        self.name = name     

    def edit_phone_number_number(self):
        phone_number = input(str("Please enter the new phone number:\n"))
        self.phone_number = phone_number

    def add_payment_method(self):
        card_number = input(str("Please enter the card number you want to add:\n"))
        self.payment_methods.append(card_number)

    def delete_payment_method(self):
        print("\nHere are the list of payment methods:\n")
        for i in range(len(self.payment_methods)):
            print(str(i+1) + ". " + self.payment_methods[i])
        card_index = input(int("Which card would you like to delete? (1 - " + str(len(self.payment_methods) + 1) + ")\n"))
        while card_index not in range(1, len(self.payment_methods) + 1):
            print("\nInvalid input. Please enter a card index that is in the list.")
            card_index = input(int("Which card would you like to delete? (1 - " + str(len(self.addresses) + 1) + ")\n"))
        self.payment_methods.pop(card_index)

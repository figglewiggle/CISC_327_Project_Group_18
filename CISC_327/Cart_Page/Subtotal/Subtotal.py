from ...models import Item
from flask import session
def subtotal():
    subtotal = 0
    cart_items = Item.query.filter_by(in_cart=True).all() # Gets all items that are in the cart
    for c in cart_items:
        price = c.price
        if session[c.id] is not None:
            price = session[c.id]
        subtotal += price # Adds all their prices 
    return subtotal

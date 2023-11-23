from ...models import Item

def subtotal():
    subtotal = 0
    cart_items = Item.query.filter_by(in_cart=True).all() # Gets all items that are in the cart
    for c in cart_items:
        subtotal += c.price # Adds all their prices 
    return subtotal

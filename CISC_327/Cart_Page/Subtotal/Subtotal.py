from models import Item

def subtotal():
    subtotal = 0
    cart_items = Item.query.filter_by(in_cart=True).all()
    for c in cart_items:
        subtotal += c.price
    return subtotal

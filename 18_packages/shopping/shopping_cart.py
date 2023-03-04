# il modulo shopping_cart essendo dentro la cartella shopping fa ora parte del package shopping
# il file __init__.py nella stessa folder di questo file è una convenzione, sta a significare che shopping è un package
print(__name__)  # shopping.shopping_cart


def buy(item):
    cart = []
    cart.append(item)
    return cart

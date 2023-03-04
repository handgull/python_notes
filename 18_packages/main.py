# import del modulo shopping_cart presente nel package shopping
# all packages are modules, but not all modules are packages.
import shopping.shopping_cart
# altro modo più diretto per accedere a buy (vale anche per i moduli)
# c'è da stare attenti ad esempio se io importassi max che esiste già tra le funzioni di py verrebbe vista solo la mia max
from shopping.shopping_cart import buy
# importo tutto da shopping_cart, meglio essere espliciti
from shopping.shopping_cart import *
print(shopping.shopping_cart)
print(shopping.shopping_cart.buy('apple'))  # ['apple']
print(buy('apple'))  # ['apple']
# __name__
print(__name__)  # __main__
if __name__ == '__main__':
    print('i am in the main file')
# https://pypi.org/ qui si trovano miriadi di package sviluppati dalla community
# pip install

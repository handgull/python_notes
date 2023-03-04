# ogni file è un module
import random  # questo è un built-in module
from collections import Counter, defaultdict, OrderedDict  # useful
import datetime  # useful
from array import array  # useful
import random as rd
import sys  # sta per system
import utility
# quando importo un file mi si crea una folder __pycache__ con il file compilato in c (se sto usanto l'interprete c)
# come cache per l'interpreter
print(utility)
print(utility.multiply(2, 2))  # 4
# built-in modules, sono un po come una standard library
# help(random)
print(dir(random))
print(random.random())  # x in the interval [0, 1]
print(random.randint(5, 10))  # int random tra 5 e 10
# Choose a random element from a non-empty sequence
print(random.choice([1, 2, 3, 4, 5]))
print(sys.argv)  # argomenti dati da terminale
# Useful Modules
li = [0, 1, 2, 3, 4, 5, 6, 7, 7]
# crea una dictionary che tiene traccia di quante volte l'item has occurred nell'iterable
print(Counter(li))
# NOTA funziona anche con le stringhe, conta le occorrenze delle lettere
# crea una dictionary con valore di default se si usa una key non presente
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['a'])
print(dictionary['c'])
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d2 = OrderedDict()
d2['a'] = 1  # se cambiassi l'ordine di questi due assegnamenti la print farebbe False
d2['b'] = 2
print(d == d2)  # True
# NOTA a quanto pare da python 3.7 le dict sono di default ordinate e quindi non serve questa classe
print(datetime.time())  # 00:00:00
print(datetime.time(5, 45, 2))  # 05:45:02
print(datetime.date.today())  # YYYY-MM-DD
arr = array('i', [1, 2, 3, 4])
print(arr)  # array è leggermente più performante di list
print(arr[0])  # posso accedere come con le list

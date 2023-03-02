# la programmazione funzionale è un altro paradigma
# separa tra loro i dati ed i comportamenti
# pure functions
# regola 1 - dando lo stesso input a una funzione pura avrò sempre lo stesso output
# regola 2 - non devono esserci side effects, non devo influenzare il mondo al di fuori della funzione
# esempio: una funzione che modifica una variabile fuori dal suo scope non è pura
from functools import reduce


def multpiply_by_2(li: list[int]):
    new_li = []  # se questa variabile fosse fuori dalla funzione sarebbe una funzione non pura
    for item in li:
        new_li.append(item*2)
    return new_li


print(multpiply_by_2([1, 2, 3]))
# quella sopra è una funzione pura


def multpiply_by_2(li: list[int]):
    new_li = []
    for item in li:
        new_li.append(item*2)
    print(new_li)


multpiply_by_2([1, 2, 3])
# quest'altra invece ha dei side effects (la print)
# btw orrendo, posso sovrascrivere le funzioni definendone una con lo stesso nome più in basso
# che poi pure il riassegnamento brutto posso fare...
hi: str = 'hi'
hi = 420
# qualcuno mi ha fermato? no nessuno e ora hi è un int. questo perchè non è strongly typed
# map, filter, zip and reduce
# map

my_list = [1, 2, 3, 4, 5]
other_list = [10, 20, 30, 40, 50, 60]


def multpiply_by_2(n: int):
    return n*2


print(list(map(multpiply_by_2, my_list)))
print(my_list)  # come si può vedere my_list non è cambiata, la funzione è pura
# filter


def check_odd(n: int):
    return n % 2 != 0


print(list(filter(check_odd, my_list)))
print(my_list)  # come si può vedere my_list non è cambiata, la funzione è pura
# zip
# zippa assieme n iterables datigli in pasto
print(list(zip(my_list, other_list)))
# NOTA il 60 è sparito perchè la lunghezza della lista di tuple è determinata dalla lunghezza dell'iterable meno lungo
# reduce


def accumulator(acc, item):
    # accumulator è una funzione non pura per colpa di questa print ma fa capire meglio
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
# lambda expressions
# one time anonymous functions that you don't need more than once
print(list(map(lambda x: x*2, my_list)))
# moltiplico tra loro tutti gli elementi della lista
print(reduce(lambda acc, item: acc*item, my_list, 1))

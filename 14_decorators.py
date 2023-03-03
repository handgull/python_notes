# Decorator pattern
# i decorators funzionano grazie alla feature di python di far funzionare le funzioni come variabili
# Higher Order Functions HOC
from time import time


def hello(func):  # è una higher order function perchè accetta in input e richiama un'altra funzione
    func()


def hello2():  # è una higher order function perchè ritorna un'altra funzione
    def func():
        return 5
    return func
# anche map filter reduce ecc sono HOC
# decorators


def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('*****')
    return wrap_func


@my_decorator
def hello():
    print('hello')


@my_decorator
def bye():
    print('bye!!')


hello()
bye()
# under the hood con i decorators viene semplicemente fatto questo:


def hello():
    print('hello')


upgraded_hello = my_decorator(hello)()

# what if - e se avessi delle funzioni con variabili? come faccio ad usarle con un decorator?


def my_decorator(func):
    # per poter far funzionare anche funzioni con parametri variabili ecc
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_func


@my_decorator
def hello(greeting: str):
    print(greeting)


hello('test')
# practical applications, esempio: creare un @performance decorator


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'{fn.__name__} function took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000):
        i*5


long_time()

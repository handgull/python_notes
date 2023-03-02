# per definire una funzione si usa def, che è una shortand per define
# DRY, Don't repeat yourself.
# Le funzioni ci aiutano quando abbiamo pezzi di codice che vogliamo richiamare più volte senza dover duplicare codice già scritto
# say_hi() se provassi a richiamare la funzione prima di definirla mi darebbe errore
def say_hi():
    '''
    Per printare il saluto la funzione oltre ad essere definita va anche chiamata
    '''
    print('hi')


say_hi()  # richiamo la funzione
# parameters vs arguments


def greets(name: str, emoji):  # se non specifico il tipo è any - ho definito una funzione con 2 positional parameters
    print(f'Helloooo {name} {emoji}')


greets('Dash', ':)')  # qui ho 2 positional arguments
greets('Josh', ':(')
# keyword arguments
greets(':(', 'Josh')
greets(emoji=':(', name='Josh')
# default parameters


# se non specifico dei valori prenderà questi
def greets_default(name='Dash', emoji='<3'):
    print(f'Helloooo {name} {emoji}')


greets_default()
greets_default('Josh', ':(')
# return


def my_sum(n1: int, n2: int):
    n1 + n2


print(my_sum(2, 2))  # None, perchè la funzione non ritorna nulla


def my_sum(n1: int, n2: int):
    return n1 + n2


print(my_sum(2, 2))  # 4


# creo una funzione dentro ad una funzione e la ritorno
def confusing_func(n1: int, n2: int):
    def wtf(n1: int, n2: int):
        return n1 + n2
        return 'dead code'  # non arriverò mai a questa riga di codice perchè c'è una return sopra
    return wtf


# questi 2 numeri non vengono usati, perchè ritorno la funzione interna e si aspetta a sua volta dei params
total = confusing_func(123, 123)
print(total(10, 20))  # 30
# help(print)  # apre vim (almeno da linux) per quittare digitare :q
# posso accedere alla doc anche tramite dunder method
print(print.__doc__)
# *args and **kwargs (keywordargs)


def super_func(*args, **kwargs):
    print(*args)
    print(kwargs)  # è una dictionary!
    print(args)  # se rimuovo l'asterisco esce una tupla!
    return sum(args)


print(super_func(1, 2, 3, hello='hello'))  # 6
# rule: params, *args, default parameters, **kwargs
# se ho dei parametri vanno prima di args, dopo di args se hanno un valore di default e kwargs va dopo tutto il resto
# Scope - what variables do i have access to?
# global_scoped - non da qui furbacchione, la variabile è accessibile da quando la si dichiara in poi
# questa variabile fa parte del global scope è accessibile da ovunque, anche dalle funzioni (guarda su)
global_scoped = True


def some_func():
    print(global_scoped)  # Yep, accessibile
    some_var = 123  # questa variabile è accessibile solo all'interno della funzione


n = 1


def confusion():
    n = 5  # se rimuovessi questa riga confusion printerebbe 1 riferendosi alla variabile globale
    print(n)


print(n)  # 1
confusion()  # 5
# as you can see there is a set of rules that the py interpreter goes through to check a variable
# First - start with local (local scope) (i parametri di funzione sono nel local scope)
# Second - parent local? cerca nello scope padre (in questo caso il global)
# Third - built-in python functions/variables/constants
# global keyword
total = 0


def count():
    global total  # senza questa keyword non potrei fare un assegnamento prima di un inizializzazione locale
    total += 1
    print(total)


count()
count()
# nonlocal keyword, molto simile a global ma prende la variabile dallo scope parent

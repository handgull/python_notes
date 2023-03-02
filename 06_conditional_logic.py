understood = True
if understood:
    print('Yep first if statement done')
else:
    print("You don't undestand?")

partially_understood = True
if not understood:
    print('Not understood')
elif True and partially_understood:  # qui ci vanno espressioni booleane, possono essere formate da tante cose unite da and, or ecc
    print("mmm not bad but you can do better")
# NOTA elif sta per else if
# Truthy vs falsey
if 'hello':  # come si può vedere dalla print la stringa hello viene castata a bool under the hood, ed è True
    print(bool('hello'))
    print(bool([]))


def my_big_messy_documentation():
    '''
    Falsy Values
    Sequences and Collections:

    Empty lists []
    Empty tuples ()
    Empty dictionaries {}
    Empty sets set()
    Empty strings ""
    Empty ranges range(0)
    Numbers

    Zero of any numeric type.
    Integer: 0
    Float: 0.0
    Complex: 0j
    Constants

    None
    False
    '''


# Ternary operator
print("Gotcha" if understood else "wtf is going on")
# Short circuiting
# True, ignoro tutto quello che c'è dopo, tanto ho ricevuto già un True e all'or ne basta uno
print(True or False)
# False, ignoro tutto quello che c'è dopo il false, perchè a and serve tutto a True
print(False and True)
# Elenco logical operators
# and or not, già visti sopra
# < > <= >=
print(5 > 4)  # True
print(1 < 2 < 3 < 4 > 5)  # False, tutto vero tranne l'ultima condizione
# == !=
# True, posso comparare le stringhe in python senza usare metodi a parte
print('hello' == 'hello')
# is vs ==
li = [1, 2, 3]
li2 = li
# True, controllo solo che i valori siano uguali. E lo sono
print(li == [1, 2, 3])
# False, controllo che il luogo occupato in memoria sia lo stesso
print(li is [1, 2, 3])
print(li == li)  # True
print(li == li2)  # True
# False, anche se sono liste vuote sono inizializzate in posti diversi
print([] is [])
print('1' is '1')  # True

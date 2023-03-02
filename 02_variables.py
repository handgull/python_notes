# variables
# le variabili devono rispettare lo snake case
# possono iniziare in lower case o con _
# i nomi di variabile possono essere formati solo da lettere, numeri ed _
# i nomi sono case sensitive
# i nomi non possono sovrascrivere le keywords del linguaggio. non posso avere una variabile che si chiama if
# i nomi devono essere descrittivi (è una cavolata ma aiuta molto la code readability)
# constants
# in py non ci sono le costanti che danno errore se si prova a fare un riassegnamento
PI = 3.14
PI = 0
# per convenzione le costanti si scrivono in CONSTANT_CASE
# dunder variables __dunder__
# quando le variabili iniziano (e finiscono) con __ sono dette dunder variables, normalmente non andrebbero mai create dallo sviluppatore
# multiple assignments
a, b, c = 1, 2, 3  # assegno contemporaneamente 3 valori diversi a 3 variabili diverse
print(a)
print(b)
print(c)
a, b, c = [1, 2, 3]  # idem partendo da una list
print(a)
print(b)
print(c)
# list unpacking
a, b, *other = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
# questa variabile conterrà tutti i numeri apparte 1 e 2, assegnati ad a e b
print(other)

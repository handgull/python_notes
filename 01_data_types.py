# Fundamental data types
v1 = 5  # int
# NOTA v1 è una variabile, in pratica le variabili sono un luogo dove conservare pezzi di informazione(valori)
v1_1 = int('111', base=2)  # il valore intero in base 10 di 111 è 7
# int() è una built-in function di python
# NOTA potevo mettere anche la stringa 0b111 al posto di 111 semplicemente 0b indica che il numero è in binario
print('2 + 2 = ' + str(2 + 2))
print(v1_1)  # 7
print(bin(v1_1))  # stampa la stringa di rappresentazione binaria dell'int
print(2 ** 3)  # 2 alla terza fa 8
# piccola parentesi sulla precedenza degli operatori, in ordine di importanza di esecuzione:
# ()
# **
# * /
# + -
print(2 // 4)  # divisione intera, 2 / 4 farebbe 0.5 quindi fa 0
print(2 % 4)  # il resto della divisione intera (in questo caso è 2)
print(type(v1_1))  # <class 'int'> il tipo di v1_1 è int
v2 = 5.0  # float
v2_1 = float('5')  # parso la stringa 5 in un float
# <class 'float'> la somma tra un int e un float viene castata automaticamente in float
print(type(2 + 2.1))
# some math functions
print(round(3.9))  # 4, arrotondo per eccesso
print(abs(-420))  # 420
v3 = True  # bool
v3_1 = bool('False')  # parso la stringa False in un bool
print(v3_1)  # True: ogni valore diverso da False o 0 senza gli apici diventa True
v4 = 'str'  # str
v4_1 = str('str')  # parsing inutile
v4_2 = str(100)  # type conversion, sto convertendo un int in una string
# riassegno lo stesso valore ma questa volta uso i doppi apici (equivalenti)
v4 = "str"
# uso la escape sequence per poter avere una stringa contenente un apice ed uno slash
v4_3 = 'stringa che usa \' e anche \\'
v4_3 += ' e ci aggiungo un \t tab e una \nnuova riga'
print(v4_3)
print(len(v4_3))  # stampa la lunghezza della stringa
# NOTA andare a rivedere l'hello world (versione estesa con il boolean mason a true)
# per rivedere i concetti di concatenazione e di string interpolation
v4_4 = 'stringa con valori come {} e anche {} dentro di loro'.format(
    123, 123.0)  # altro metodo, più scomodo di fare una formatted string
print(v4_4)
v4_4 = 'stringa con valori come {1} e anche {0} dentro di loro'.format(
    123, 123.0)  # così do un ordine diverso
print(v4_4)
v4_4 = 'stringa con valori come {var1} e anche {var2} dentro di loro'.format(
    var1=123, var2=123.0)  # uso delle variabili per referenziare i valori
print(v4_4)
# NOTA non c'è storia, la string interpolation con f davanti è 100 volte meglio
long_string = '''
WOW
o o
---
'''  # per avere lunghe stringhe che vanno su linee multiple
print(long_string)
# le stringhe "under the hood" sono conservate come sequenze di caratteri
v4_5 = '123456'
# concatena velocemente delle stringhe passandogli un iterable di stringhe
print('? '.join(['a', 'lot', 'of', 'questions']))
#       012345
# [start:stop:stepover] -> concetto googlabile come slicing o string slicing
print(v4_5[3])  # 4
print(v4_5[0:3])  # 123
print(v4_5[0:7:2])  # 135
print(v4_5[0:])  # 123456
print(v4_5[:5])  # 12345
print(v4_5[-1])  # 6 parto dalla fine della stringa
print(v4_5[-2])  # 5
# reverse della stringa/lista -> NOTA le liste hanno anche .reverse() che lo fa in place
print(v4_5[::-1])
# strings immutability
# posso riassegnare totalmente una stringa, ma non posso (al contrario delle liste) fare questo:
# string[3] = 'n'
# string methods
# a differenza delle funzioni i metodi appartengono ad un tipo, sia esso un tipo base o una classe
print(v4_4.upper())
print(v4_5.replace('1', '2'))  # replace ritorna la nuova stringa
# come si può vedere la stringa resta immutata perchè non ho fatto un assegnamento
print(v4_5)
print('*' * 5)  # *****
print('yes' in 'there is a yes word here')  # True
li = [1, 2, 3, 4, 5]  # list
li2 = [1, '2', True]  # list di "dynamic" come direbbe mio cuggino dash
# NOTA: battuta perchè dash è la mascotte di dart/flutter e lì il tipo indefinito si chiama dynamic
# le list sono le prime data structures che abbiamo visto fino ad ora
# list slicing = string slicing già affrontato
# nelle liste posso riassegnare i valori in corrispondenza di un determinato indice (al contrario delle stringhe)
li[2] = 2
print(li)  # [1, 2, 2, 4, 5]
li3 = li  # creo una nuova lista? NO creo una nuova reference alla vecchia lista
li3[2] = 3
print(li)  # [1, 2, 3, 4, 5] infatti modificando li3 si modifica anche li
# NOTA una veloce soluzione grazie allo slicing potrebbe essere questo:
li4 = li[:]  # li[:] restituisce una nuova lista perfettamente uguale a li
li4 = li.copy()  # stessa cosa ma usando un list method
# Matrix, liste multi dimensionali
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 2, ho acceduto al secondo elemento della prima sottolista
print(matrix[0][1])
print(len(matrix))  # 3
# cambia in place la lista stessa, e come si vede dall'ide restituisce None
li.append(6)
print(6 in li)  # True, ho aggiunto il 6 giusto appena sopra
li.append(1)
print(sorted(li))  # genera una nuova lista sortata
li.sort()  # sorta in place
# range da 1 a 11 (quando diventa una lista lo stop non conta quindi questa sarà una list da 1 a 10)
range = range(1, 11)
print(range)  # printo l'iterable di tipo range
print(list(range))  # converto il range in una list
# NOTA guardare il file delle variabili per la feature di unpacking collegata alle list
dict  # Dictionary, un altra data structure: una coppia chiave valore non ordinata. i dati quindi non sono salvati in memoria in modo adiacente
# tramite la key ho accesso immediato al valore, senza dover ciclare (cosa che faremo in una la list) alla ricerca
# quello qui sotto è un dict[str, str] ma come le list i value possono essere di tipo diverso, sia per la key che per il value
# tranne list, una key di una dict non può essere una lista
# posso confrontare la struttura di un dictionary semplicemente facendo ==
dictionary = {
    'key1': 'value1'
}
print(dictionary['key1'])
dictionary = {
    'key1': 'value1',
    'key1': 'value2',
}
# value2, value1 viene sovrascritto una key dovrebbe essere unica
print(dictionary['key1'])
# se nel dict sopra dovessi fare
# print(dictionary['key2'])
# il programma andrebbe in errore, e gli errori vanno gestiti. Per evitare questo si può usare
print(dictionary.get('key2'))  # None
print(dictionary.get('key2', 55))  # 55
print(dictionary.get('key2'))  # None
# esiste un altro modo di inizializzare dei dict, meno comodo secondo me ed è tramite la built-in function dict
print(dict(name='Josh'))
print('key1' in dictionary)  # True
# False, il valore era stato sovrascritto
print('value1' in dictionary.values())
# ritorna una lista di tuple (le si vede fra poco) che compongono il dictionary
print(dictionary.items())
print(dictionary.keys())  # ritorna la lista di key del dict
tuple  # immutable list, meno flessibilità ma meno error prone se si vuole dare dei limiti
my_tuple = (1, 2, 3)  # come le stringhe è immutable
print(my_tuple[1])  # 2
set  # collection of unique objects, unordered
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)  # {1, 2, 3, 4, 5} stampa una sola volta il 5
li5 = [1, 2, 3, 4, 5, 5]
print(list(set(li5)))  # passaggio utile per eliminare duplicati da una lista
# i set non supportano l'indexing (sono unordered appunto) quindi my_set[0] da errore
# NOTA i set hanno il vantaggio di avere funzioni di insiemistica, ne faccio vedere solo alcune qui
my_set = {0, 1, 2, 3}
other_set = {1, 2, 3, 4, 5}
print(other_set.difference(my_set))  # {4, 5}
print(other_set.intersection(my_set))  # {1, 2, 3}
print(other_set & my_set)  # short hand per la intersection
print(other_set.union(my_set))  # {0, 1, 2, 3, 4, 5}
print(other_set | my_set)  # short hand per la union
# None, assenza di valore
# extra data type: complex per la matematica complessa

# Classes -> custom data types

# Specialized data types, moduli utili con tipi built-in

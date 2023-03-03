# quick way to create list, set or dictionaries
# list comprehensions
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)  # ['h', 'e', 'l', 'l', 'o']
my_list = [char for char in 'hello']  # one liner equivalente a sopra
print(my_list)  # ['h', 'e', 'l', 'l', 'o']
my_list = [n*2 for n in range(0, 5)]  # moltiplico ogni elemento per 2
print(my_list)  # [0, 2, 4, 6, 8]
my_list = [n for n in range(0, 5) if n % 2 == 0]  # aggiungo solo i pari
print(my_list)  # [0, 2, 4]
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# oneliner per avere la lista di duplicati (passo da set per non avere ripetizioni)
duplicates = list(set([x for x in my_list if my_list.count(x) > 1]))
print(duplicates)  # ['b', 'n']
# set and dictionary Comprehension
# per i set si possono fare le stesse identiche cose delle list ma con { } al posto delle [ ]
simple_dict = {
    'a': 1,
    'b': 2,
}
# creo una dictionary partendo da un altra dictionary dove elevo ogni value al quadrato
my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)  # {'a': 1, 'b': 4}
my_dict = {str(value): value for value in [1, 2, 3]}  # partendo da una list
print(my_dict)  # {'1': 1, '2': 2, '3': 3}

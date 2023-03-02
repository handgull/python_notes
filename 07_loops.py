# Posso iterare qualsiasi cosa che abbia una collezione di elementi (list, set ecc)
for item in 'Dash':
    print(item)
print(item)  # item è accessibile anche a ciclo finito, cosa un po bruttina
# naturalmente posso nestare i cicli
for i in [1, 2, 3]:
    for j in ['a', 'b', 'c']:
        print(i, j)
# iterable, what does it means?
# sono iterable le stringhe, le list, i set, le tuple i dictionary... i range...
# in parole povere tutto ciò che può essere iterato ovvero andare one by one con i suoi valori
new_dict = dict(key1='value1')
for key, value in new_dict.items():
    print(key, value)
# range
for index in range(0, 10):
    print(index)
for index in range(10, 0, -1):  # il -1 è lo stepover, funziona come negli slices
    print(index)
for _ in range(0, 10):
    print('I don\' care about the index')
# enumerate
for i, item in enumerate('Dash'):  # grazie ad enumerate posso ottenere l'index
    print(i, item)
# while loops
i = 0
while i < 3:  # qualsiasi espressione booleana va bene
    print(i)
    i += 1  # non esistono ++ e -- che tristezza
# questo viene eseguito nel momento in cui la condizione diventa falsa (l'else del while è opzionale)
else:
    print('Done!')
while True:
    print('omg infinite loop')
    # don't worry lo stoppo in modo brusco tramite keyword break (funziona anche nei for)
    break
else:
    print('Done!')  # non verrà mai eseguito, anche se esco dal ciclo con break
# continue and pass
for index in range(0, 10):
    continue
    # nothing will be printed -> continue dice al ciclo ignora tutte le righe sotto questa e continua a ciclare
    print(index)
# pass non serve a niente, può essere utile come placeholder per tenere chiuso un ciclo che ancora non si sa come implementare

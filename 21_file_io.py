my_file = open('test.txt')
print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
# oggetto TextIOWrapper, nome file, modalità di lettura, encoding
print(my_file.read())  # leggo il contenuto del file
print(my_file.read())
my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
print(my_file.readlines())
my_file.seek(0)
print(my_file.readlines())
my_file.close()  # va fatto sempre se si decide di leggere i files in questa maniera
# better way with the built-in with statement
with open('test.txt') as my_file:
    print(my_file.readlines())
# NOTA non devo chiudere il file in questa maniera
# Read, Write, Append
# mode r+ -> legge e scrive contemporaneamente, mode a -> aggiunge il testo al testo già esistente
# con r+ se il file non esiste ho un errore
# con w se il file che sto cercando di aprire non esiste lo crea
with open('test.txt', mode='w') as my_file:
    my_file.write('ups!')
    my_file.seek(0)  # riporto il cursore a 0 quindi sovrascrivo ups
    my_file.writelines(['scemo chi legge\n', ':)\n', 'lol2'])
# pathlib is a useful lib when it comes to handle relative paths on different systems
# NOTA in teoria ora windows funziona anche con gli / quindi no problem imo

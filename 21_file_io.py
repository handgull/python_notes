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
my_file.close()

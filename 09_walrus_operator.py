# introdotto da py 3.8
# what: new syntax for assigning variables in the middle of expressions
str1 = 'helloooooo'
while (length := len(str1)) > 0:  # assegno a length la lunghezza MENTRE comparo la lunghezza
    print(length, str1)
    str1 = str1[:-1]  # tolgo l'ultimo char alla stringa

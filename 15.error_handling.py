# se non inserisco un numero va in type error, lo gestisco con un try except
invalid_number = True
while invalid_number:
    try:
        n = int(input('enter a number: '))
        print(n)
    except:
        print('please enter a number!')
    else:
        invalid_number = False
invalid_number = True
while invalid_number:
    try:
        n = int(input('enter a number, i will use it to divide 5: '))
        print(5/n)
    # posso "ascoltare" più errori in una singola except usando una tupla
    except (TypeError, ValueError) as err:  # mi segno il messaggio di errore in una variabile err
        print(f'please enter a number! {err}')
    except ZeroDivisionError:  # gestisco l'errore specifico di divisione
        print('infinity!')
        invalid_number = False
    else:
        invalid_number = False
    finally:  # runna a prescindere ogni volta dopo il try/except
        print('done!')

raise ValueError('mmm non mi garba sto valore')  # throwo l'errore

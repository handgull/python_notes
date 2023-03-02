# prova a far vedere a schermo un albero, partendo da questa matrice, se incontri uno 0 metti spazio
# se incontri un 1 metti l'asterisco
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


for image in picture:
    for pixel in image:
        if pixel:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

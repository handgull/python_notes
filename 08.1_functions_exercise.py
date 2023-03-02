# data una lista di numeri fare una funzione per trovare il più alto numero pari
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 1, 2, 3, 4, 8]))

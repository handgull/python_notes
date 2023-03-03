# Here is an example generator which calculates fibonacci numbers:
# generator version
def gen_fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in gen_fib(10):
    print(x)

# same thing but with comprehension
print([n for n in gen_fib(10)])


def procedural_fib(number):
    a = 0
    b = 1
    result = []
    for _ in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


# se dovessi fare un fib di 100000 ci metterebbe anni e forse crasherebbe
print(procedural_fib(10))
# grazie ai generators anche se ci mette anni a finire mi fornisce il risultato a ogni iterazione
for x in gen_fib(100000):
    print(x)

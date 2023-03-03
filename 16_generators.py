# iterable
# __iter__ -> ogni iterable ha questo dunder
# generators are iterables, sono un subset. range è un generator
# i generators sono funzioni speciali che ritornano un lazy iterator, non vengono salvati in memoria

def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(10):
    print(item)

g = generator_function(5)
print(g)  # come si può vedere g è un oggetto generator
print(next(g))  # con next posso iterare
print(next(g))
print(next(g))


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator)*2)
        except StopIteration:
            break


special_for([240, 34.5, 59])

# esempio di come può essere implementato un range tutto custom grazie ad alcuni dunder methods


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # this line allows us to use the current number as the starting point for the iteration
        MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 10)
for i in gen:
    print(i)

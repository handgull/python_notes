# object oriented programming paradigm
# in python tutto è un oggetto, ogni tipo che abbiamo affrontato è costruito da python tramite la parola "class"
print(type(69))
# abbiamo diversi metodi che possiamo chiamare per performare azioni su di essi
print('dash'.upper())
# gli oggetti possono inoltre avere attributi (variabili - che siano dunder o meno)
int_var = 420
print(int_var.__doc__)
# la vera "svolta" della OOP è creare i propri oggetti e poter spezzettare grandi logiche in porzioni "a se stanti" combinabili tra loro
# ed anche estensibili
# il codice scritto con questo paradigma ha il vantaggio di essere ben organizzato anche se arriva a grandi dimensioni
# creare le proprie classi:


class MyObject:  # le classi vanno chiamate usando il PascalCase
    pass


obj1 = MyObject()  # le classi sono come una "blueprint" gli oggetti sono le istanze
print(type(obj1))


class PlayerCharacter:
    # class object attributes - sono attributi statici accessibili da tutte le istanze
    is_magician = True
    # init è un dunder/magic method, sarebbe il costruttore è chiamato in automatico ad ogni instanziamento

    def __init__(self, name, age=20) -> None:
        self.name = name  # attribute
        # in python non c'è un modo vero e proprio per definire le variabili private / renderle non modificabili ma per convenzione si mette _
        self._age = age

    def run(self):
        print(f'{self.name} is running')

    def toggle_magician(self):
        # questo toggle toggla il booleano per TUTTE le istanze della classe
        PlayerCharacter.is_magician = not PlayerCharacter.is_magician

    @staticmethod  # metodo statico accessibile senza instanziare la classe
    def adding_things(n1, n2):
        return n1 + n2

    @classmethod  # metodo statico che crea una nuova classe del tipo PlayerCharacter e la ritorna
    def create_dash_sum(cls, n1, n2):
        return cls('Dash', n1 + n2)


player1 = PlayerCharacter('Dash')
player2 = PlayerCharacter('Josh')
print(player1)  # possiamo vedere anche la memory location dove l'istanza è salvata
print(player1.name)  # Dash
player1.run()  # Dash is running
# che schifo, posso creare nuovi attributi semplicemente assegnando qualcosa
player1.health = 100
print(player1.health)
# help(list)  # shows the class, the "blueprint" of the list objects :q per uscire
print(player1.is_magician)  # True
print(player2.is_magician)  # True
player1.toggle_magician()
print(player1.is_magician)  # False
print(player2.is_magician)  # False
print(PlayerCharacter.adding_things(2, 2))  # 4
player3 = PlayerCharacter.create_dash_sum(2, 2)
print(player3.name)  # Dash
print(player3._age)  # 4, ho potuto accedere anche se dovrebbe essere privata
# 4 pillars of OOP
# encapsulation - possibilità di accorpare metodi e proprietà all'interno di un unica area, ovvero all'interno dell'Oggetto
# abstraction - nascondere informazioni / rendere astratto il modo in cui le cose vengono svolte dando accesso solo a ciò che è necessario
# inheritance - when a class derives from another class. estendendo una classe possiamo ottenere una buona base (es archer estende player)
# polymorphism - indica la possibilità per uno stesso oggetto di assumere più forme.

# inheritance example


class User():
    def sign_in(self):
        print('logged in')


class Archer(User):
    pass


class Wizard(User):
    pass


archer = Archer()
wizard = Wizard()
archer.sign_in()
wizard.sign_in()

# True, la classe archer eredita da user per tanto è considerata anche di tipo user (questo ci permette di fare polimorfismo)
print(isinstance(archer, User))
# True, tutti gli oggetti ereditano da object
print(isinstance(archer, object))
print(isinstance(archer, Archer))  # True
print(isinstance(archer, Wizard))  # False

# polymorphism example


class Animal:
    def __init__(self, name):
        self.name = name

    # potrei anche non mettere il metodo nella classe base e chiamarlo lo stesso. Orrendo...
    def speak(self):
        return 'Some noises'


class Gatto(Animal):
    def speak(self):
        return 'Miao'


class Cane(Animal):
    def speak(self):
        return 'Bau'


a = Gatto('Fufi')
b = Gatto('Ciccio')
c = Cane('Fido')
for animal in [a, b, c]:
    print(animal.name + ': ' + animal.speak())
# Output:
#
# Fufi: Miao
# Ciccio: Miao
# Fido: Bau

# super()


class Car():
    def __init__(self, name):
        self.name = name


class Ferrari(Car):
    def __init__(self, name):
        # chiamo il costruttore di Car nel costruttore di Ferrari
        super.__init__(name)
        # Car.__init__(self, name) metodo alternativo e più brutto di fare la stessa cosa


# introspection
print(dir(Ferrari))
# Dunder methods


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f"color: {self.color}, age: {self.age}"

    def __len__(self):
        return 420  # len deve ritornare per forza un integer

    def __del__(self):
        return "deleted"

    def __call__(self):
        return ('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure)
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
del action_figure
# Multiple inheritance -> è una porcata, sappi che esiste ma meglio non usarla poi ci va di mezzo anche la MRO (Method Resolution Order)

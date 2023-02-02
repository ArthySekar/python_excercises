class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'You are talking to {self.name}')


point = Person('Arthy')
print(point.name)
point.talk()


bob = Person('Bob')
bob.talk()


class Mammal:
    def talk(self):
        print('talk')


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


point1 = Dog()
point1.talk()
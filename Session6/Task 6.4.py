# Task 6.4
# Create hierarchy out of birds.
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.
# Implement str() function call for each class.

class Bird:

    def __init__(self, name):
        self._name = name

    def fly(self):
        return print(f'{self._name} bird can fly\n')

    def walk(self):
        return print(f'{self._name} bird can walk\n')


class FlyingBird(Bird):

    def __init__(self, name, ration):
        self._name = name
        self._ration = ration

    def eat(self):
        return print(f"{self._name} eats usually {self._ration}\n")


class NonFlyingBird(FlyingBird):

    def __init__(self, name):
        self._name = name
        self._ration = "Ass"

    def fly(self):
        return print(f"{self._name} don't fly\n")

    def __str__(self):
        return str(self._name) + " can walk and fly \n"


class SuperBird(NonFlyingBird):

    def __init__(self, name):
        self._name = name
        self._ration = "Cannibal"

    def __str__(self):
        return str(self._name) + "can fly, walk and swim\n"


a = Bird("Mike")
a.walk()
a.fly()

b = FlyingBird("Lol", "Meat")
b.eat()
b.walk()
b.fly()

c = NonFlyingBird("Scot")
print(str(c))
c.fly()
c.eat()

d = SuperBird("Pipindor")
print(str(d))
d.eat()
d.walk()
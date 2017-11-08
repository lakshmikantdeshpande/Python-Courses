class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s" % (self.name, thing))

    def show_affection(self):
        print('%s wags tail' % (self.name))


class Cat(Animal):
    def swatstring(self):
        print("%s shreds the string" % (self.name))

    def show_affection(self):
        print('%s purrs' % (self.name))


for _ in (Dog('Travor'), Cat('Loo')):
    _.show_affection()

from pinject import Pinject

class Dog:
    def bark(self):
        print('woof')


class Cat:
    def meow(self):
        print('meow')


container = Pinject() \
    .add(Dog).as_singleton() \
    .add(Cat).as_singleton() \
    .build()


class Showcase:
    def __init__(self, container):
        self.cat = container.Cat
        self.dog = container.Dog
    
    def make_sounds(self):
        self.cat.meow()
        self.dog.bark()


Showcase(container).make_sounds()
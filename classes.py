from abc import ABC
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Wooff')

class Cat(Animal):
    def make_sound(self):
        print('Meoow')

class Mouse(Animal):
    def make_sound(self):
        print('Squeek')
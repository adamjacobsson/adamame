from abc import ABC
from abc import ABC, abstractmethod
import random

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self) -> None:
        self.number = self.r_n()

    def make_sound(self):
        print('Wooff')
    
    def r_n(self):
        return random.randint(1, 9)


class Cat(Animal):
    def __init__(self) -> None:
        self.number = self.r_n()

    def make_sound(self):
        print('Meoow')
    
    def r_n(self):
        return random.randint(1, 9)


class Mouse(Animal):
    def __init__(self) -> None:
        self.number = self.r_n()

    def make_sound(self):
        print('Squeek')
    
    def r_n(self):
        return random.randint(1, 9)
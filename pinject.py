from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Callable
from custom_types import ContainerDict


class InstanceType(ABC):
    @abstractmethod
    def provide(self):
        raise NotImplementedError


class Singleton(InstanceType):
    def __init__(self, callable: Callable) -> None:
        self._callable = callable
    
    def provide(self):
        print('Singleton provide')


class Transient(InstanceType):
    def __init__(self, callable: Callable) -> None:
        self._callable = callable
    
    def provide(self):
        print('Transient provide')


class ContainerObject:
    def __init__(self, callable: Callable) -> None:
        self.callable = callable
        self.type = None
    
    def as_singleton(self):
        self.type = Singleton(callable=self.callable)
        return self

    def as_transient(self):
        self.type = Transient(callable=self.callable)
        return self


class Pinject:
    def __init__(self) -> None:
        self.container = ContainerDict()

    def add(self, callable: Callable = None):
        c_o = ContainerObject(callable=callable)
        self.container[callable.__name__] = c_o
        return c_o
    
    def build(self):
        self.container.instances = self.container

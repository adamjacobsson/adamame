from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Callable
from custom_types import AttrDict, Singleton, Transient


class InstanceType(ABC):
    @abstractmethod
    def provide(self):
        raise NotImplementedError

"""
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
"""

class Pinject:
    def __init__(self) -> None:
        self.container = AttrDict()
        self._callable = None

    def add(self, callable: Callable = None):
        self._callable = callable
        return self

    def build(self):
        pass
        #self.container.instances = self.container

    def as_singleton(self):
        self.container[self._callable.__name__] = {
            'callable': self._callable(),
            'instance_type': 'singleton'
        }

    def as_transient(self):
        self.container[self._callable.__name__] = {
            'callable': self._callable,
            'instance_type': 'transient'
        }
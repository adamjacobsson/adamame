from typing import Callable


class AttrDict(dict):
    def __getattr__(self, attr):
        item = self[attr]['callable']
        instance_type = self[attr]['instance_type']
        return item if instance_type == 'singleton' else item()


class Pinject:
    def __init__(self) -> None:
        self.container = AttrDict()
        self._callable = None

    def add(self, callable: Callable = None):
        self._callable = callable
        return self

    def build(self):
        return self.container

    def as_singleton(self):
        self.container[self._callable.__name__] = {
            'callable': self._callable(),
            'instance_type': 'singleton'
        }
        return self

    def as_transient(self):
        self.container[self._callable.__name__] = {
            'callable': self._callable,
            'instance_type': 'transient'
        }
        return self
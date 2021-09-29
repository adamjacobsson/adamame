from pinject import Pinject
from classes import Dog, Cat, Mouse

pinject = Pinject()
pinject.add(Dog).as_singleton()
pinject.add(Cat).as_singleton()
pinject.add(Mouse).as_singleton()

pinject.build()

pinject.container.Dog().make_sound()
print('ee')

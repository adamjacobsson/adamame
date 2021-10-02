class SomeTest:
    def __init__(self, container) -> None:
        self.dog = container.Dog
        self.cat = container.Cat
        self.mouse = container.Mouse

    def some_sound(self):
        self.dog.make_sound()
    
    def numbers(self):
        print(self.dog.number)
        print(self.cat.number)
        print(self.mouse.number)


class SomeTestTwo:
    def __init__(self, container) -> None:
        self.dog = container.Dog
        self.cat = container.Cat
        self.mouse = container.Mouse

    def some_sound(self):
        self.dog.make_sound()
    
    def numbers(self):
        print(self.dog.number)
        print(self.cat.number)
        print(self.mouse.number)

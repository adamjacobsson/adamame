from sstate import Sstate


class Test1:
    def __init__(self, state) -> None:
        self.state = state
    
    def add_attr(self, k, v):
        self.state[k] = v

class Test2:
    def __init__(self, state) -> None:
        self.state = state

    def add_attr(self, k, v):
        self.state[k] = v

s = Sstate()

t1 = Test1(Sstate())
t2 = Test2(Sstate())

t1.add_attr('hej', 'hehe')
t2.add_attr('då', 'meme')

print(s['hej'])
s.pop('hej')
print(t1.state)
print(t2.state)
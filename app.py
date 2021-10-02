from pinject import Pinject
from classes import Dog, Cat, Mouse
from test import SomeTest, SomeTestTwo


def main():
    container = build_container()
    t = SomeTest(container=container)
    for _ in range(5):
        t.numbers()
    print('--------')
    tt = SomeTestTwo(container=container)
    for _ in range(5):
        tt.numbers()

def build_container():
    return Pinject() \
        .add(Dog).as_singleton() \
        .add(Cat).as_singleton() \
        .add(Mouse).as_transient() \
        .build()


if __name__ == '__main__':
    main()

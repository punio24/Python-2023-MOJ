class MyClass:
    i = 12345

    def __init__(self, n):          # __init__ jest konstruktorem wywolawczym w klasach
        self.n = n

    def f(self):
        return f'hello world {self.n}'


o1 = MyClass(1)         # zmienna ma przypiwsana myClassey (1)
o2 = MyClass(4)         # zmienna ma przypiwsana myClassey np wartosc (4)

o1

o1.i                    # po kropka jest odwolaniem do zmiennej
o2.i
o1.n
o2.n
o1.f()                  # tu przypisywane sa wartosci z podstawionych klas do zmiennej
o2.f()


class MyClass:
    i = 0

    def __init__(self, n):
        self.i+=1
        self.n = n

    def f(self):
        print(self)
        return f'hello world {self.n}'

    @classmethod
    def get_i(cls):
        print(cls)
        return cls.i

o1 = MyClass(1)
o2 = MyClass(2)

o1.i
o2.i
o1.n
o2.n
o1.f()
o2.get_i()



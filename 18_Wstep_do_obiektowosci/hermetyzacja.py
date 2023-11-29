class Employee:
    pass


john = Employee()

john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

john.salary


class Employee:
    def __init__(self, name, dept, salary):
        self.__name = name                  # pola z __ sa zastrzezone, hermetyzacja , zamkniecie dostepu elementow klasy, aby ktos z zewnatrz
        self.__dept = dept                  # nie mogl sie dostac - ale juz wewnatrz klasy tak, np uprawnienia do podgladu wyplat
        self.__salary = salary

    def get_salary(self):
        return self.__salary


john = Employee('John Doe', 'computer lab', 1000)
john.__salary  # error

john.get_salary()

john._Employee__salary

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def r(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


p = Point(3.0, 4.0)
p
print(p.r)
p.r = 7  # error

# Anatomia obiektu

print(p.__dict__)
print(Point.__dict__)

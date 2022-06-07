#Задание 1

class Matrix:

    def __init__(self, data_mtx):
        self.data_mtx = data_mtx

    def __str__(self):
        return '\n'.join('\t'.join(map(str, i)) for i in self.data_mtx)

    def __add__(self, other):
        for i in range(len(self.data_mtx)):
            for j in range(len(self.data_mtx[i])):
                self.data_mtx[i][j] = self.data_mtx[i][j] + other.data_mtx[i][j]
        return Matrix.__str__(self)


a_1 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
a_2 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(a_1 + a_2)

# Задание 2
from abc import ABC, abstractmethod

class Сlothes(ABC):

    @abstractmethod
    def calculate_one(self):
        pass

    def calculate_all(one, other):
        return (one.v / 6.5 + 0.5) + (other.h * 2 + 0.3)


class Coat(Сlothes):

    def __init__(self, v=0):
        self.v = v

    @property
    def calculate_one(self):
        return self.v / 6.5 + 0.5


class Suit(Сlothes):

    def __init__(self, h=0):
        self.h = h

    @property
    def calculate_one(self):
        return self.h * 2 + 0.3

a = Coat(2)
b = Suit(3)

print(a.calculate_one)
print(b.calculate_one)
print(Сlothes.calculate_all(a, b))

#Задание 3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(33)
cells2 = Cell(9)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)

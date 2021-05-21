'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для формирования
матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.'''


 class Matrix:
     def __init__(self, input_data):
         self.input = input_data

     def __str__(self):
         return '\n'.join([' '.join(map(str, line)) for line in self.input])

     def __add__(self, other):
         answer = ''
         if len(self.input) == len(other.input):
             for line_1, line_2 in zip(self.input, other.input):
                 if len(line_1) != len(line_2):
                     return 'Problems with shape'

                 summed_line = [x + y for x, y in zip(line_1, line_2)]
                 answer += ' '.join(map(str, summed_line)) + '\n'
         else:
             return 'Problems with shape'
         return answer


 matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
 matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
 print(matrix_1)
 print()
 print(matrix_1 + matrix_2)  # matrix_1.__add__(matrix_2)

'''2. Реализовать проект расчета суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих 
методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные 
на этом уроке знания: реализовать абстрактные классы для основных классов 
проекта, проверить на практике работу декоратора @property.'''

 from abc import ABC, abstractmethod

 class Clothes(ABC):
     def __init__(self, param):
         self.param = param

     @abstractmethod
     def calculate(self):
         pass


 class Coat(Clothes):

     @property
     def calculate(self):
         return round((self.param / 6.5) + 0.5)


 class Suit(Clothes):

     @property
     def calculate(self):
         return round((2 * self.param) + 0.3)


 coat = Coat(45)
 suit = Suit(170)
 print(coat.calculate)
 print(suit.calculate)

'''3. Реализовать программу работы с клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству 
клеток (целое число). В классе должны быть реализованы методы перегрузки
арифметических операторов: 
сложение (add()), 
вычитание (sub()), 
умножение (mul()),
деление (truediv()).
Данные методы должны выполнять увеличение,уменьшение, умножение и 
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
В классе необходимо реализовать метод make_cell(), принимающий экземпляр класса 
и количество клеток в ряду. Метод должен возвращать строку виду **\n\n**..., 
где количество клеток между \n равно переданному аргументу, а количество рядов
определяется, исходя из общего количества клеток.
При создании экземпляра клетки должна происходить перезапись параметра, 
который хранит количество клеток.'''

 class Cell:
     def __init__(self, nums):
         self.nums = nums

     def make_order(self, rows):
         return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
                + '\n' + '*' * (self.nums % rows)

     def __str__(self):
         return str(self.nums)

     def __add__(self, other):
         return 'Sum of cell is ' + str(self.nums + other.nums)
         # return Cell(self.nums + other.nums)

    def __sub__(self, other):
         return self.nums - other.nums if self.nums - other.nums > 0 \
             else 'Ячеек в первой клетке меньше или равно второй, вычитание невозможно'

     def __mul__(self, other):
         return 'Multiply of cells is ' + str(self.nums * other.nums)

     def __truediv__(self, other):
         return 'Truediv of cells is ' + str(round(self.nums / other.nums))


cell_1 = Cell(10)
cell_2 = Cell(34)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(10))
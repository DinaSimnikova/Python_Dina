"""
1.
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Date(object):

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def number(cls, date):
        day, month, year = map(int, date.split('-'))
        date_1 = cls(day, month, year)
        print (cls, date)
        return date_1

    @staticmethod
    def valid_date(date):
        day, month, year = map(int, date.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 2021:
            print(date)
            return day, month, year
        else:
            print('Ошибка ввода данных')

d = '36-12-2021'
date2 = Date.number(d)
is_date = Date.valid_date(d)

"""
2
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверить его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(Exception):
    def __init__(self, number):
        self.number = number

def div():
    try:
        user_num_1 = int(input('Введите делимое: '))
        user_num_2 = int(input('Введите делитель: '))
        if user_num_2 == 0:
            raise OwnError("На 0 делить нельзя!")
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(div())

"""
3
Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
"""

"""
4
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. 
"""

"""
5
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники 
на склад и передачу в определенное подразделение компании. Для хранения данных 
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать 
любую подходящую структуру, например словарь.
"""

"""
6
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных 
на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» 
максимум возможностей, изученных на уроках по ООП.
"""

class Storage:
    def __init__(self, name):
        self.name = name
        self._dict = {}

    def work(self):
        print(f'{self.name} is working')

    def add_to(self, equipment):
            ''' добавляем в словарь обьект по его названию, в значении
            будет список экземпляров этого оборудования'''
            self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
            ''' извлекаем из значения обьект по названию группы.
            дальше можно расширить поиск по серии, марки или еще чему либо'''
            if self._dict[name]:
                self._dict.setdefault(name).pop(0)

class Equipment:
    def __init__(self, name, model, price, *args):
        self.name = name
        self.model = model
        self.price = price
        self.printer_dict = {}
        self.scaner_dict = {}
        self.xerox_dict = {}
        self.items = {'Название устройства': self.name, ' Модель': self.model, 'Стоимость': self.price}
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.model} {self.price}'

    def work_working(self):
        print(f'{self.name} is working')

class Printer(Equipment):
    def __init__(self, name, model, price, *args):
        super().__init__(name, model, price, *args)
        self.printer_dict = []

class Scan(Equipment):
   def __init__(self, name, model, price, *args):
        super().__init__(name, model, price)
        self.scaner_dict = []

class Xerox(Equipment):
    def __init__(self, name, model, price, *args):
        super().__init__(name, model, price)
        self.xerox_dict = []

sklad = Storage('New_Storage')
# создаем объект и добавляем
scaner = Scan('Sony', '567', 45600)
sklad.add_to(scaner)
printer = Printer('HP', '689', 34500, 2018)
sklad.add_to(printer)
# выводим склад
print(sklad._dict)
# забираем с склада и выводим склад
sklad.extract('Printer')
print()
print(sklad._dict)


"""
7
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные 
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. 
"""

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

num_1 = ComplexNumber(5, 7)
num_2 = ComplexNumber(9, 6)
print(num_1 + num_2)
print(num_1 * num_2)
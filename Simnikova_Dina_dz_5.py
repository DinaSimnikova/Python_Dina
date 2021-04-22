"""
1
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
"""
import sys

def odd_nums(number):
    for num in range(1, number + 1, 2):
        yield num

odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))

"""
2
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), 
не используя ключевое слово yield.
"""

number = 15
odd_to_number = (num for num in range(1, number + 1, 2))

print(next(odd_to_number))

"""
3

"""

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

from itertools import zip_longest

tutor_for_klass = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))

print(type(tutor_for_klass))
print(next(tutor_for_klass))

"""
4
Представлен список чисел. Необходимо вывести те его элементы, значения которых 
больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке. Подумайте, 
как можно сделать оптимизацию кода по памяти, по скорости.
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(result)

"""
5
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, 
например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

src2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_src2 = [el for el in src2 if src2.count(el) == 1]
print(unique_src2 )


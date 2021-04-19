"""
Задание 2
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в
обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную
задачу? Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы
с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""
import requests
from decimal import *
from datetime import datetime

getcontext().prec = 4

def currency_rates(val):
    val = val.upper()
    answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in answer:
        return None

    rub = answer[answer.find('<Value>', answer.find(val)) + 7:answer.find('</Value>', answer.find(val))]
    day_raw = answer[answer.find('Date="') + 6:answer.find('"', answer.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{(Decimal(rub.replace(',', '.')))}, {datetime(day=day, month=month, year=year)}"


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('eur'))

"""
Задание 4 
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. 
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). 
Убедиться, что ничего лишнего не происходит.
"""

import utils
print(utils.currency_rates('EUR'))
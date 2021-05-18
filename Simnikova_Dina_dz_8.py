"""
Task 1
Написать функцию email_parse(<email_address>), которая при помощи
регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и
возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}

email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
"""

import re

EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')

def email_parse(email):
    email_info = EMAIL.findall(email)[0]
    if email_info:
        name, domain = email_info
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, domain)

email_parse('petr2020@geekbrains.ru')
# email_parse('igor1997@geekbrainsru')

"""
Task2
*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера
из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида:
(<remote_addr>,
<request_datetime>,
<request_type>,
<requested_resource>,
<response_code>,
<response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
"""

import re
import requests

PARSING = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                 r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                 r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
content = requests.get(url).text
for args in PARSING.findall(content):
    addr, datetime, type, resource, code, size = args
    print(addr, datetime, type, resource, code, size)

"""
# Task4
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные 
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
"""

from functools import wraps


def val_checker(decorator_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapped(x):
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)

        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """calc_cube desc"""
    return x ** 3

a = calc_cube(5)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)

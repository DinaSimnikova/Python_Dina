"""
Задание 1
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
логов web-сервера nginx_logs.txt
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
"""

with open('nginx_log.txt') as parsing:
    new_list = []
    for line in parsing:
        splitted = line.split()
        new_list.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
    print(new_list)

"""
Task 2
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла 
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать 
даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

with open('nginx_log.txt') as f:
    data = []
    spam_dict = {}
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam_dict.setdefault(splitted[0], 0)
        spam_dict[splitted[0]] += 1

spam_dict = max(spam_dict.items(), key=lambda x: x[1])
print('task_2')
print(spam_dict)

"""
Task 3 
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. 
Известно, что при хранении данных используется принцип: одна строка — один пользователь, 
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов 
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в 
файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, 
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с 
кодом «1». При решении задачи считать, что объём данных в файлах во много 
раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби  (hobby.csv):
скалолазание,охота
горные лыжи
"""

from itertools import zip_longest
import json
out_dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobbies.csv', encoding='utf-8') as hobbies:
        lines_in_users = sum(1 for line in users)
        lines_in_hobbies = sum(1 for line in hobbies)

        if lines_in_users < lines_in_hobbies:
            exit(1)

        users.seek(0)
        hobbies.seek(0)
        for line_user, line_user_hobby in zip_longest(users, hobbies):
            out_dict[line_user.strip()] = line_user_hobby.strip() if \
                line_user_hobby is not None else line_user_hobby

with open('task3.json', 'w', encoding='utf-8') as file:
    json.dump(out_dict, file, ensure_ascii=False)
print(out_dict)

"""
Task 6 - не разобралась с решением
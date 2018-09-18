
# Задание

#     Создайте список словарей:

#             [
#             {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
#             {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
#             {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
#         ]

#     Запишите содержимое списка словарей в файл в формате csv


import csv

# Создайте список словарей
user_list = [ {'name': 'Маша', 'age': 25, 'job': 'Scientist'} ]
user_list.append( {'name': 'Вася', 'age': 8, 'job': 'Programmer'} )
user_list.append( {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'} )
user_list.append( {'name': 'Даша', 'age': 14, 'job': 'Pupil'} )
user_list.append( {'name': 'Гена', 'age': 63, 'job': 'Teacher'} )
user_list.append( {'name': 'Саша', 'age': 22, 'job': 'Student'} )

#     Запишите содержимое списка словарей в файл в формате csv
with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = [ 'name', 'age', 'job' ]
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow( user )

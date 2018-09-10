
# Задание

#     Создайте такой словарь:
#     {"city": "Москва", "temperature": "20"}
#     Выведите на экран значение по ключу city
#     Уменьшите значение "temperature" на 5
#     Выведите на экран весь словарь

my_dic = {'city' : 'Москва', 'temperature' : '20'}
print( my_dic['city'])
my_dic['temperature'] = int( my_dic['temperature'] ) - 5
print( my_dic )


# Задание

#     Проверьте, есть ли в словаре ключ country
#     Выведите значение по-умолчанию "Россия" для ключа country
#     Добавьте в словарь элемент date со значением '27.05.2017'
#     Выведите на экран длину словаря

print( my_dic.get( 'country' ) )
print( my_dic.get( 'country', 'Россия' ) )
my_dic['date'] = '27.05.2017'
print( len( my_dic ) )
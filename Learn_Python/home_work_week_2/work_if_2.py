
# Практика: Сравнение строк

#     Написать функцию, которая принимает на вход две строки
#     Проверить, является ли то что переданно функции строками. Если нет - вернуть 0
#     Если строки одинаковые, верунть 1
#     Если строки разные и первая длиннее, вернуть 2
#     Если строки разные и вторая строка 'learn', возвращает 3
#     Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты

def check_str( str1, str2):
    if type(str1) != str or type(str2) != str :
        return 0
    elif str1 == str2:
        return 1
    elif str1 != str2 and len(str1) > len(str2) and str2 != 'learn':
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3


print (check_str(9, 'python'))              #      >>> 0
print (check_str('python', 'python'))       #      >>> 1
print (check_str('learn_python', 'python')) #      >>> 2
print (check_str('python', 'learn'))        #      >>> 3
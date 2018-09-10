# Задание 2

#     Создайте в Sublime файл price.py
#     Создайте функцию format_price которая принимает один аргумент price
#     Приведите price к целому числу (тип int)
#     Верните строку "Цена: ЧИСЛО руб."
#     Вызовите функцию, передав на вход 56.24 и положив результат в переменную display_price
#     Выведите display_price на экран

def format_price( price ):
    price = int( price )
    return "Цена: {} руб.".format( price )

display_price = format_price( 56.24 )
print( display_price )
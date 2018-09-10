# price = 100
# vat_rate = 18

# vat = price / 100 * vat_rate
# print( vat )

# ======================================================

price = 100
vat_rate = 18

vat = price / 100 * vat_rate
price_no_vat = price - vat
print( price_no_vat )

# ======================================================

# Создадим функцию
# Функция принимает два значения. Первое - цена, второе - процент
# Выводит на экран цену без процента
def get_vat(price, vat_rate):
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    print(price_no_vat)

price1 = 100
vat_rate1 = 18
get_vat(price1, vat_rate1)
        

# Задание 1

#     Измените функцию get_summ() чтобы результат выводился заглавными буквами использйте метод 'строка'.upper()
#     Вызовите функцию, пердав в нее два аргумента "Learn" и "python"
#     Сохраните результат вызова функции в переменную sum_string
#     Выведите на экран значение переменной

# Исходная функция выглядит так

# def get_summ(one, two, delimiter='&'):
#     return str(one) + str(delimiter) + str(two)
                        

def get_summ(one, two, delimiter='&'):
    return str(one).upper() + str(delimiter) + str(two).upper()

sum_string = get_summ( 'Learn', 'Python')
print( sum_string )






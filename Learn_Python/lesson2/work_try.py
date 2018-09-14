
# Задание

#     Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
#     Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение типов не сработало


def get_summ(num_one, num_two):

    try:
        return int( num_one ) + int( num_two )
    except (ValueError, TypeError):
        return "Будте бдительны, Вы ввели не целые числа."


print( get_summ( 235, 89 ) )        # >>>  324
print( get_summ( 'dfs', 43 ) )      # >>>  Будте бдительны, Вы ввели не целые числа
print( get_summ( 32.34, 345 ) )     # >>>  377
print( get_summ( 33, False ) )      # >>>  33
print( get_summ( 33, '22' ) )       # >>>  55
print( get_summ( (), 89 ) )         # >>>  Будте бдительны, Вы ввели не целые числа

# Практика: Возраст

#     Попросить пользователя ввести возраст при помощи input и положить результат в переменную
#     Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
#     Вызвать функцию, передав ей возраст пользователя и положить результат работы функции в преременную
#     Вывести содержимое переменной на экран



# Функция проверяет данные, которые ввел пользователь. Если это не число, то возвращает False
def isint( val ):
    try:
        int( val )
        return True
    except ValueError:
        return False


# Проверяем данные, которые ввел пользователь. Если это не число, то запрашиваем у пользователя до тех пор, пока он не введет нужную нам информацию
def correct_value( val_age ):
    # если ввели не целочисленные данные, то просим повторить ввод
    while not isint( val_age ):
        val_age = input('Вы ввели некорректно Ваш возраст!\nВведите Ваш возраст: ')

        # проверяем диапазон вводимыx данных по возрасту от 0 до 150
        if isint( val_age ) and ( int(val_age) < 0 or int(val_age) > 150 ):
            val_age = ''
    
    return int( val_age )   # Преобразуем переменную в целочисленный тип и возвращаем ее обратно


# функция, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
def busy( value ):
    # Переменная которая возвращается
    busy_men = ''
    if value == 0 or value == 1:
        busy_men = 'Агу-агу-гу-гу-гу'
    elif value == 2:
        busy_men = 'Ma, pa, tutu'
    elif value >= 3 and value < 7:
        busy_men = 'У всех была первая любовь в детском саду.'
    elif value >= 7 and value < 18:
        busy_men = 'Школа - это прекрасная пора. Учись и развивайся.'
    elif value >= 18 and value < 25:
        busy_men = 'Пройди подготовительные курсы для взрослой жизни. Сходи в армию, получи вышнее образование.'
    elif value >= 25 and value < 60:
        busy_men = 'Жизнь прекрасна. Живи, люби, воспитывай и не забывай учиться.'
    elif value >= 60 and value < 100:
        busy_men = 'Поздравляю, вы не многие, кто дожил до второго детства.'
    elif value >= 100 and value < 145:
        busy_men = 'Вы долгожитель. Эти аплодисметы Вам. Жаль, что в этом возрасте слух подводит.'
    elif value >= 145 and value <= 150:
        busy_men = 'Ваше настоящее имя Дункан Маклауд. Берегите свою голову!!!'

    return busy_men




# Запрашиваем у пользователя его возраст
age = correct_value( input( 'Введите Ваш возраст: ') )



#     Вызвать функцию, передав ей возраст пользователя и положить результат работы функции в преременную
user_busy = busy(age)

#     Вывести содержимое переменной на экран
print(user_busy)


# Задание

#     Скачайте файл по ссылке
#     Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
#     Подсчитайте количество слов в тексте
#     Замените точки в тексте на восклицательные знаки
#     Сохраните результат в файл referat2.txt


# Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
with open("referat.txt", "r", encoding='utf-8') as file:
    read_file = file.read()

# Длинна получившейся строки
len_file = len( read_file )
print( len_file )               #  >>>  1509

# Подсчитайте количество слов в тексте
word_file = read_file.split()
len_word = len( word_file )
print( len_word )               #   >>>  163

# Замените точки в тексте на восклицательные знаки
read_file = read_file.replace('.', '!')

# Сохраните результат в файл referat2.txt
with open('referat2.txt', 'w') as f:
    f.write( read_file ) 
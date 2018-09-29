# Updater - это компонент отвечающий за коммуникацию с сервером Telegram
# именно он получает / передает сообщения. 
# CommandHandler --> обработчик комманд

# MessageHandler,Filters --> обработчики текстовых сообщений

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Импортируем модуль ephem для того, чтобы можно было определить в каком созвездии находится 
# интересующая нас планета
import ephem

# Импортируем модуль datetime, для того, чтобы определять дату ЗДЕСЬ и СЕЙЧАС
import datetime

# Импортируем необходимые модули для клавиатуры 
# from aiogram.types import ReplyKeyboardMarkup

# Настройки прокси

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


# Добовляем ключ от бота из тайного файла
with open("key_bot.txt", "rt") as f:
    key_bot = f.read()

# записываем отчет о работе бота в отдельный файл, чтобы можно было проверять его работу
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# Функция вызывается, когда пользователь в чате напишит /start 
# вручную или подключится к боту в первый раз
# update.message.reply_text(text) --> посылает сообщение обратно в Telegram

def greet_user(bot, update):
    text = 'Я готов тебя слушать =)'
    update.message.reply_text(text)

# Функция "отвечает" пользователю эхом
def talk_to_me(bot, update):
    user_text = update.message.text 
    update.message.reply_text(user_text)

# ============================= Планеты =================================

# Функция "отвечает" пользователю при вводе /planet ...
def talk_planet(bot, update):
    
    # Получаем от юзера сообщение и складываем в список
    user_text = update.message.text.split()

    # Ответ пользователю если он неверно ввел планету
    text = 'Такого космического тела нет!'

    # Проверяем полученое сообщение
    if user_text[0] == '/planet':

        # Определяем календарную дату
        date = datetime.datetime.now()

        # Приводим введенную планету в корректную форму
        user_text[1] = user_text[1].lower().capitalize()

        # Проверяем второе слово через getattr и если это не планета, то ловим ошибку
        try:
            user_planet = getattr( ephem, user_text[1] ) 
        except AttributeError:
            update.message.reply_text( text )
            return

        # Определяем нахождение космического тела
        position = user_planet( date )

        # Отправляем пользователю сообщение
        update.message.reply_text( 'Космическое тело сейчас находится в созвездии {}'.format( str(ephem.constellation( position ))) )

# Функция ведет подсчет введеных слов пользователя 
def len_text(bot, update):
    """
        Функция подсчитвает кол-во слов присланных от пользователя
    """
    # Получаем от юзера сообщение
    user_text = update.message.text

    # Определяем индекс первого вхождения кавычки
    try:
        first_index = user_text.index('"')
        our_text = user_text[first_index + 1:]
    except ValueError:
        update.message.reply_text("Поставьте в начале и в конце предложения кавычки")
        return

    # Определяем индекс второго вхождение кавычек
    try:
        second_index = our_text.index('"')
        our_text = our_text[:second_index]
    except ValueError:
        update.message.reply_text("Поставьте в начале и в конце предложения кавычки")
        return

    # Разделяем полученый текст
    text_split = our_text.split()
    update.message.reply_text("Вы ввели {} слов".format( len(text_split)))


# Функция калькулятор
def calcul(bot, update):
    
    # Полученное сообщение от пользователя
    user_text = update.message.text.split()

    # Арифметические знаки
    symbol = '+-*/'

    # проверка на то, чтобы в конце был знак '='
    if not user_text[-1] == '=':
        update.message.reply_text('Поставте в конце знак "=" (равно)')
    elif not user_text[2] in symbol:
        update.message.reply_text('Такого "{}" нет математического знака'.format( user_text[2] ))
    elif user_text[2] == '/' and user_text[3] == 0:
        update.message.reply_text('На ноль делить нельзя. Это может делать, только Чак Норис.')
    elif user_text[2] == '+':
        try:
            return update.message.reply_text(int(user_text[1]) + int( user_text[3] ) ) 
        except:
            update.message.reply_text('Я могу работать только с целыми числами.')
    elif user_text[2] == '-':
        try:
            return update.message.reply_text(int(user_text[1]) - int( user_text[3] ) )
        except:
            update.message.reply_text('Я могу работать только с целыми числами.')
    elif user_text[2] == '*':
        try:
            return update.message.reply_text(int(user_text[1]) * int( user_text[3] ) ) 
        except:
            update.message.reply_text('Я могу работать только с целыми числами.')
    elif user_text[2] == '/' and user_text[3] != 0:
        try:
            return update.message.reply_text(int(user_text[1]) / int( user_text[3] ) ) 
        except:
            update.message.reply_text('Я могу работать только с целыми числами.')
        


# ===================================Тело бота =============================


# Функция, которая соединяется с платформой Telegram

def main():
    mybot = Updater(key_bot, request_kwargs=PROXY)

    # Диспечер бота
    dp = mybot.dispatcher

    # вызываем функцию, которая будет подключаться к Telegram и отправлять сообщение обратно
    dp.add_handler(CommandHandler("start", greet_user))

    # Добавляем в бота команду /planet, которая будет принимать на вход название планеты на английском, например /ephem Mars
    dp.add_handler(CommandHandler("planet", talk_planet))

    # вызываем функцию, которая будет подсчитывать кол-во слов
    dp.add_handler(CommandHandler("wordcount", len_text))

    # вызов функции калькулятор
    dp.add_handler(CommandHandler("calcul", calcul))

    # вызываем функцию, которя "отвечает" пользователю на сообщение тем же сообщением
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
       
# Вызываем функцию - эта строчка запускает бота

main()

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

# Настройки прокси

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


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
    text = 'Вызван /start. Я готов тебя слушать =)'
    update.message.reply_text(text)

# Функция "отвечает" пользователю
def talk_planet(bot, update):
    
    # Получаем от юзера сообщение
    user_text = update.message.text

    # складываем в список полученное сообщение, разделяя пробелом
    user_text = user_text.split(' ')

    # Проверяем полученое сообщение
    if user_text[0] == '/planet':

        # Определяем календарную дату
        date = datetime.datetime.now()

        # Определяем название планеты и выводим в сообщение в каком созвездии сегодня находится планета.
        if user_text[1] == 'Sun':
            sun = ephem.Sun(date)
            update.message.reply_text(ephem.constellation(sun))
        elif user_text[1] == 'Mars':
            mars = ephem.Mars(date)
            update.message.reply_text(ephem.constellation(mars))
        elif user_text[1] == 'Mercury':
            mercury = ephem.Mercury(date)
            update.message.reply_text(ephem.constellation(mercury))
        elif user_text[1] == 'Venus':
            venus = ephem.Venus(date)
            update.message.reply_text(ephem.constellation(venus))
        elif user_text[1] == 'Jupiter':
            jupiter = ephem.Jupiter(date)
            update.message.reply_text(ephem.constellation(jupiter))
        elif user_text[1] == 'Saturn':
            saturn = ephem.Saturn(date)
            update.message.reply_text(ephem.constellation(saturn))
        elif user_text[1] == 'Uranus':
            uranus = ephem.Uranus(date)
            update.message.reply_text(ephem.constellation(uranus))
        elif user_text[1] == 'Neptune':
            neptune = ephem.Neptune(date)
            update.message.reply_text(ephem.constellation(neptune))
        elif user_text[1] == 'Pluto':
            pluto = ephem.Pluto(date)
            update.message.reply_text(ephem.constellation(pluto))
    else:
        update.message.reply_text("Я могу выводить только в каком созвездии сегодня находится планета.")
    
    
# ===================================Тело бота =============================


# Функция, которая соединяется с платформой Telegram

def main():
    mybot = Updater("636051867:AAGCi__yUUF3kKj4JmkCl52-1wfr4IbztJw", request_kwargs=PROXY)

    # Диспечер бота
    dp = mybot.dispatcher

    # вызываем функцию, которая будет подключаться к Telegram и отправлять сообщение обратно
    dp.add_handler(CommandHandler("start", greet_user))

    # Добавляем в бота команду /planet, которая будет принимать на вход название планеты на английском, например /ephem Mars
    dp.add_handler(CommandHandler("planet", talk_planet))

    # вызываем функцию, которя "отвечает" пользователю на сообщение тем же сообщением
    dp.add_handler(MessageHandler(Filters.text, talk_planet))

    mybot.start_polling()
    mybot.idle()
       
# Вызываем функцию - эта строчка запускает бота

main()

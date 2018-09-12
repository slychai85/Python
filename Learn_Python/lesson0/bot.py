# Updater - это компонент отвечающий за коммуникацию с сервером Telegram
# именно он получает / передает сообщения. 
# CommandHandler --> обработчик комманд

# MessageHandler,Filters --> обработчики текстовых сообщений

from telegram.ext import Updater, CommandHandler, MessageHandler,Filters

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
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

# Функция "отвечает" пользователю
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
    
# ===================================Тело бота =============================


# Функция, которая соединяется с платформой Telegram

def main():
    mybot = Updater("", request_kwargs=PROXY)

    dp = mybot.dispatcher

    # вызываем функцию, которая будет подключаться к Telegram и отправлять сообщение обратно
    dp.add_handler(CommandHandler("start", greet_user))

    # вызываем функцию, которя "отвечает" пользователю на сообщение тем же сообщением
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
       
# Вызываем функцию - эта строчка запускает бота

main()

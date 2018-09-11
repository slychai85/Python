# Updater - это компонент отвечающий за коммуникацию с сервером Telegram
# именно он получает / передает сообщения.
from telegram.ext import    Updater, 
                            CommandHandler # импорт обработчика комманд


# Настройки прокси

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}



# import logging
# logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO,
#                     filename='bot.log'
#                     )



# ===================================Тело бота =============================


# Функция, которая соединяется с платформой Telegram

def main():
    mybot = Updater("", request_kwargs=PROXY)
    mybot.start_polling()
    mybot.idle()
       
# Вызываем функцию - эта строчка собственно запускает бота

main()

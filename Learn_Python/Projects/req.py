import requests

# requests.get() - получение результата запроса
# функция, принимает url и возвращает строку ответа
# добавляем второй параметр params для того, чтобы соствать url
def get_html( url, params={}):
    # отлавливаем ошибки при запросе к серверу
    try:
        # переменная, в которой хранится ответ запроса
        result = requests.get( url, headers={'User-Agent': 'Mozilla/5.0'}, params=params )
        # проверка статуса кода ответа от сервера
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestsWarning as e:
        print('Ошибка при запросе: {}'.format(e))
        return False


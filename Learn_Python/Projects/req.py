import requests

# requests.get() - получение результата запроса
# функция, принимает url и возвращает строку ответа
def get_html( url ):
    # отлавливаем ошибки при запросе к серверу
    try:
        # переменная, в которой храниться ответ запроса
        result = requests.get( url, headers={'User-Agent': 'Mozilla/5.0'} )
        # проверка статуса кода ответа от сервера
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestsWarning as e:
        print( 'Ошибка при запросе: {}'.format( e ) )
        return False


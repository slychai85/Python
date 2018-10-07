import requests

def get_html(url):
    # проверка статуса ответа
    try:
        result = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException as e:
        print ( e )
        return False



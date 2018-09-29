import requests

# Функция выводит результат запроса url
def get_weather( url ):
    result = requests.get( url )
    if result.status_code == 200:
        return result.json()
    else:
        print("Где-то ошибка")

# Если функцию вызываем напрямую, то вызываем наш url
if __name__ == "__main__":
    data = get_weather( "http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=be37def33fbf342b7cb451e62381a38c&units=metric")
    print( data )



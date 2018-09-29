import requests

# Функция выводит результат запроса url
def get_weather( url ):
    result = requests.get( url )
    print( result.text )

# Если функцию вызываем напрямую, то вызываем наш url
if __name__ == "__main__":
    get_weather( "http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=be37def33fbf342b7cb451e62381a38c" )



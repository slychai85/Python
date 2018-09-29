from datetime import datetime
from flask import Flask

# Импортирую свою функцию
from req import get_weather

# Переменные для подставления в url
city_id = 524901
apikey = "be37def33fbf342b7cb451e62381a38c"

# Переменная которая содержит каркас приложения (создание приложения)
app = Flask(__name__)

# Главная страница
@app.route("/")

# Обработчик для адреса
def index():
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % ( city_id, apikey )
    weather = get_weather( url )
    cur_date = datetime.now().strftime('%d.%m.%Y')
    result = "<p><b>Температура:</b> %s</p>" % ( weather['main']['temp'])
    result += "<p><b>Город:</b> %s</p>" % ( weather['name'] )
    result += "<p><b>Дата:</b> %s</p>" % ( cur_date )
    return result

# Если запускается напрямую, его нужно запустить
if __name__ == "__main__":
    app.run()
  

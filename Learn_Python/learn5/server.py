from datetime import datetime
from flask import Flask, abort, request

# Импортирую свою функцию
from news_list import all_news
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

# Обработка переменных
@app.route( "/news" )
def all_the_news( ):
    colors = ['green', 'red', 'blue', 'white']
    try:
        limit = int(request.args.get( 'limit', 'all' ))
    except:
        limit = 11
    color = request.args.get('color') if request.args.get('color') in colors else 'black'
    return '<h1 style="color: %s">News: <small>%s</small></h1>' % ( color, limit )

# Для создания новостных страниц
@app.route( "/news/<int:news_id>")
def news_by_id( news_id ):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len( news_to_show ) == 1:
        result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>"
        result = result % news_to_show[0]
        return result
    else:
        abort(404)


# Если запускается напрямую, его нужно запустить
if __name__ == "__main__":
    app.run()
  

from flask import Flask, render_template, request
from table_users import User
from table44 import Zakupki44
# request нужен для того, чтобы принимать данные со странице

# Переменная которая содержит каркас приложения (само приложение)
app = Flask(__name__)

# Обработчик для главной страницы
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Good Day')

# Обработчик для страницы с таблицей, ограниченый одним методом
@app.route('/table/', methods=['GET', 'POST'])
def table():
    data = Zakupki44.query.all()
    return render_template('table.html', items=data, title='Good Day')
 

# items=Zakupki44.query.all()
# Если этот файл запускается на прямую, то нужно запустить приложение
if __name__ == '__main__':
    app.run(port=5010, debug=True)



   # fz_44 = request.form.get('fz_44')
    # if fz_44 == 44:
    # data = Zakupki44.query.all()
    # Проверка введеных данных
    # return render_template('table.html', items=Zakupki44.query.all())

    # if User.query.filter(User.email == request.form.get('email')).first():
    #     print(Zakupki44.query.all())
    #     return render_template('table.html', items=Zakupki44.query.all())
            # email=request.form.get('email'),
            # fz_44=request.form.get('fz_44'), 
            # fz_223=request.form.get('fz_223'),
            # fz_185=request.form.get('fz_185'), 
            # time_since=request.form.get('time_since'),
            # time=request.form.get('time'))
        #  render_template('index.html')
    # else:
    #     return redirect("/")
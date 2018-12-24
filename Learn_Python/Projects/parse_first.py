from bs4 import BeautifulSoup
import sqlite3
import sqlalchemy
# Работа с датой, нужно чтобы получать дату здесь и сейчас
from datetime import datetime
# Импорт функции, которая находится в req, для того, чтобы получить html сайта
from req import get_html
# Импортируем base_table.db для того, чтобы добавлять данные с гланой страницы
from base_table import db_session, BaseZakupki


# Переменная хранит дату сегодняшнего дня в правильном формате url
dt_now = datetime.now()
# Составляем параметры url, чтобы составить правильный запрос
params = {
        'pageNumber': 1,
        'recordsPerPage': '_10',
        'fz44': 'on',
        'fz223': 'on',
        'ppRf615': 'on',
        'pc': 'on',
        'updateDateFrom': dt_now.strftime('%d.%m.%Y'),
        'updateDateTo': dt_now.strftime('%d.%m.%Y')
}
# html поисковой страницы сайта Госзакупки
search_html = 'http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html'

#  Получение html страницы документа
html = get_html(search_html, params)
# Парсинг страницы
bs = BeautifulSoup(html, 'html.parser')

list_fz = []
list_id = []
# Пробую пока только на одной странице, а после этого нужно будет добавить цикл
# Поиск на странице нужных данных и добавление их в базу данных
for item in bs.find_all('span', class_='orange'):
    free_list = item.text
    free_list = free_list.split('-')
    list_fz.append(free_list[0])

# id
for item in bs.find_all('td', class_='descriptTenderTd'):

    free_list = item.find('dt').text
    free_list = free_list.split()
    # Проверка на длину id, если он короче 6, то это не id 
    if len(free_list[1]) > 5:
        list_id.append(free_list[1])


def write_any_way (db_session, data):
    """
    написать функция кот будет писать в базу (котрые будет перехватывать ошибки перезаписи)        
    """
    try:
        # Добавляем в сессию data (данные с сайта)
        db_session.add(data)
        db_session.flush()
    except sqlalchemy.exc.IntegrityError as e:
        db_session.rollback()
        print(e)
    


# Проверка на то одинаковое кол-во полученных данных
if len(list_fz) == len(list_id):
    # Если все верно, то запускаем цикл на добавление данных в БД
    # Иначе запускаем --> надо подумать, что с этим делать
    for item in range(len(list_id)):
        my_data = BaseZakupki(list_id[item], list_fz[item])
        # Добавляем в сессию data (данные с сайта)
        write_any_way(db_session, my_data)
    db_session.commit()
else:
    print('Длинна не совпадает: ' + str(len(list_fz)) + ' = ФЗ ' + str(len(list_id)) + ' = id')

# try:
#     db_session.commit()
# except:
#     pass

# db_session.commit()

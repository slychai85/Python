import sqlite3
import sqlalchemy
# Импортируем base_table.db для того, чтобы добавлять данные с гланой страницы
from base_table import db_session, BaseZakupki
from bs4 import BeautifulSoup
# Работа с датой, нужно чтобы получать дату здесь и сейчас
from datetime import datetime
# Импорт функции, которая находится в req, для того, чтобы получить html сайта
from req import get_html


# Переменная хранит дату сегодняшнего дня
dt_now = datetime.now()
# Составляем параметры url, чтобы составить правильный запрос
params = {
    'pageNumber': 1,
    'recordsPerPage': '_50',
    'fz44': 'on',
    'fz223': 'on',
    'ppRf615': 'on',
    'pc': 'on',
    'updateDateFrom': dt_now.strftime('%d.%m.%Y'),
    'updateDateTo': dt_now.strftime('%d.%m.%Y')
}
# html поисковой страницы сайта Госзакупки
search_html = 'http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html'
list_fz = []
list_id = []


for page in range(1, 11):
    # На каждой новой итерации меняем номер страницы
    params['pageNumber'] = page
    #  Получение html страницы документа
    html = get_html(search_html, params)
    # Парсинг страницы
    bs = BeautifulSoup(html, 'html.parser')

    # Разделяем странцу на отдельные участки
    for item in bs.find_all('div', class_='registerBox'):
        # Поиск номера закона
        free_fz = item.find('span', class_='orange').text
        # Проверка законов - имеют разное построение слов
        if free_fz[0] == 'П':
            free_fz = free_fz.split()
            fz = free_fz[2]
        else:
            free_fz = free_fz.split('-')
            fz = free_fz[0]
        # Поск id
        id_item = item.find('td', class_='descriptTenderTd')
        free_id = id_item.find('dt').text
        free_id = free_id.split()
        # Проверка id на имеющиеся в БД
        if BaseZakupki.query.filter(BaseZakupki.id_zakupki == free_id[1]).first():
            break
        elif len(free_id[1]) > 5:
            list_id.append(free_id[1])
            list_fz.append(fz)


# Запускаем цикл на добавление данных в БД
for item in range(len(list_id)):
    my_data = BaseZakupki(list_id[item], list_fz[item])
    db_session.add(my_data)

db_session.commit()

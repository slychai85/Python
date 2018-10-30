from bs4 import BeautifulSoup
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

for item in bs.find_all('td', class_='descriptTenderTd'):
    free_list = item.text
    free_list = free_list.split()
    list_id.append(free_list[1])


# Проверка на то одинаковое кол-во полученных данных
if len(list_fz) == len(list_id):
    print(list_fz[len(list_fz)-1])
    # Если все верно, то запускаем цикл на добавление данных в БД
    # Иначе запускаем --> надо подумать, что с этим делать
    for item in range(0, len(list_id)-1):
        print(list_id[item])
        my_data = BaseZakupki(list_id[item], list_fz[item], dt_now.strftime('%d.%m.%Y %H:%M'))
        # Добавляем в сессию data (данные с сайта)
        db_session.add(my_data)

db_session.commit()


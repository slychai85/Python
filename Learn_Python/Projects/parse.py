from bs4 import BeautifulSoup
# Работа с датой, нужно чтобы получать дату здесь и сейчас
from datetime import datetime

# Импорт функции, которая находится в req, для того, чтобы получить html сайта
from req import get_html

# Переменная хранит дату сегодняшнего дня
dt_now = datetime.now()

# Составляем переменные url, чтобы составить правильный запрос
# af=on - подача заявок
# ca=on - работа комиссии
# pc=on - процедура завершена
# pa=on - процедура отменена
params = {
        'pageNumber': 1,
        'recordsPerPage': '_50',
        'fz44': 'on',
        'fz223': 'off',
        'ppRf615': 'off',
        'af': 'off',
        'ca': 'off',
        'pc': 'on', 
        'pa': 'off',
        'updateDateFrom': dt_now.strftime('%d.%m.%Y'),
        'updateDateTo': dt_now.strftime('%d.%m.%Y')
}

# html страница Госзакупок по закону 44-ФЗ с сегодняшней датой обновления
for item in range(1, 20):
    params['pageNumber'] = item
    html = get_html('http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html', params=params)

    # Парсим страницу
    bs = BeautifulSoup( html, 'html.parser')

    # Проходим циклом и вытягиваем ссылки на тендеры
    for item in bs.find_all('td', class_='descriptTenderTd'):
        href = item.find('a')
        print(href.get('href'))

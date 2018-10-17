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
# priceFromGeneral - minimum price
# priceToGeneral - max price
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
        'updateDateTo': dt_now.strftime('%d.%m.%Y'),
        'priceFromGeneral': '1000000',
        'priceToGeneral': ''
}
test_params = {
        'pageNumber': 1,
        'recordsPerPage': '_50',
        'fz44': 'on',
        'pc': 'on', 
        'updateDateFrom': dt_now.strftime('%d.%m.%Y'),
        'updateDateTo': dt_now.strftime('%d.%m.%Y'),
        'priceFromGeneral': 100000000,
        'priceToGeneral': 1000000000
}
url = 'http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html?pageNumber={0}&recordsPerPage={1}&fz44={2}&pc={3}&priceFromGeneral={4}&priceToGeneral={5}&updateDateFrom=17.10.2018&updateDateTo=17.10.2018'.format(test_params['pageNumber'], test_params['recordsPerPage'], test_params['fz44'], test_params['pc'], test_params['priceFromGeneral'], test_params['priceToGeneral'])
# html страница Госзакупок по закону 44-ФЗ с сегодняшней датой обновления
# for item in range(1, 20):
#     params['pageNumber'] = item
html = get_html(url)

# Парсим страницу
bs = BeautifulSoup( html, 'html.parser')

# Проходим циклом и вытягиваем ссылки на тендеры
for item in bs.find_all('td', class_='descriptTenderTd'):
    href = item.find('a')
    try:
        print(href.get('href'))
    except AttributeError as e:
        print('Ошибка при запросе: {}'.format( e ) )

urlllll = 'http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html?pageNumber={0}&recordsPerPage={1}&fz44={2}&pc={3}&priceFromGeneral={4}&priceToGeneral={5}&updateDateFrom={6}&updateDateTo={7}'.format(test_params['pageNumber'], test_params['recordsPerPage'], test_params['fz44'], test_params['pc'], test_params['priceFromGeneral'], test_params['priceToGeneral'], test_params['updateDateFrom'], test_params['updateDateTo'])
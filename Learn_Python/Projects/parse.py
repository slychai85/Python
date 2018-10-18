from bs4 import BeautifulSoup
# Работа с датой, нужно чтобы получать дату здесь и сейчас
from datetime import datetime
# Импорт функции, которая находится в req, для того, чтобы получить html сайта
from req import get_html

# Переменная хранит дату сегодняшнего дня
dt_now = datetime.now()
# Начало ссылки 
short_link = 'www.zakupki.gov.ru'
# Переменная будет хранить все нужные ссылки
list_links = [];
# Переменная для записи id которые выдали ошибку
error_links = []
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
        'priceToGeneral': '2222222222'
}
for item in range(1, 20):
    test_params = {
        'pageNumber': item,
        'recordsPerPage': '_50',
        'fz44': 'on',
        'pc': 'on', 
        'updateDateFrom': dt_now.strftime('%d.%m.%Y'),
        'updateDateTo': dt_now.strftime('%d.%m.%Y'),
        'priceFromGeneral': '100000000',
        'priceToGeneral': '1000000000'
    }
    html = get_html('http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html', params=test_params)
    # Парсим страницу
    bs = BeautifulSoup( html, 'html.parser')
    # Проходим циклом и вытягиваем ссылки на тендеры
    for item in bs.find_all('td', class_='descriptTenderTd'):
        href = item.find('a')
        try:
            list_links.append(href.get('href'))
        except:
            error_links.append(href)

for link in list_links:
    common_url = short_link + link
    print(common_url)
    htmls = get_html(common_url, params=params)
    bs = BeautifulSoup(htmls, 'html.parser')
    for item in bs.find_all('td', class_ = 'noticeTdFirst fontBoldTextTd'):
        if item == 'Способ определения поставщика (подрядчика, исполнителя)':
            info = item.find_next_sibling('td')
            print(info)
# http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html?pageNumber=1&recordsPerPage=_50&fz44=on&fz223=on&ppRf615=on&af=on&ca=on&pc=on&pa=on&priceFromGeneral=1111111111&priceToGeneral=22222222222&updateDateFrom=18.10.2018&updateDateTo=18.10.2018
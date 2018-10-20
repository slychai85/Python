from bs4 import BeautifulSoup
# Работа с датой, нужно чтобы получать дату здесь и сейчас
from datetime import datetime
# Импорт функции, которая находится в req, для того, чтобы получить html сайта
from req import get_html

# Переменная хранит дату сегодняшнего дня
dt_now = datetime.now()
# Начало ссылки, нужна для того, чтобы перейти к документу
short_link = 'http://www.zakupki.gov.ru'
# Переменная будет хранить все нужные ссылки на документы
list_links = []
# Общий словарь всех нужных данных
list_dct = []
# Список необходимых полей на главной страницы документа
keys_44fz = [
        'Способ определения поставщика (подрядчика, исполнителя)',
        'Размещение осуществляет',
        'Сведения о связи с позицией плана-графика',
        'Начальная (максимальная) цена контракта',
        'Место доставки товара, выполнения работы или оказания услуги',
        'Сроки поставки товара или завершения работы либо график оказания услуг',
        'Размер обеспечения исполнения контракта',
# документы - все ссылки на странице находятся в классе ' attachment' class displayTable
# Результаты определения поставщика - название победитенля и его организационно правовая форма
# Журнал событий - Дата извещения о проведении аукциона
]

# Запуск парсинга страницы поиска с необходимыми значения
for item in range(1, 20):

    test_params = {
        'pageNumber': item,
        'recordsPerPage': '_50',
        'fz44': 'on',
        'pc': 'on', 
        'updateDateFrom': dt_now.strftime('%d.%m.%Y'),
        'updateDateTo': dt_now.strftime('%d.%m.%Y'),
        'priceFromGeneral': '100000',
        'priceToGeneral': '100000'
    }
    html = get_html('http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html', params=test_params)
    # Парсим страницу
    bs = BeautifulSoup( html, 'html.parser')

    # Проходим циклом и вытягиваем ссылки на тендеры
    for item in bs.find_all('td', class_='descriptTenderTd'):

        # Получение ссылок
        href = item.find('a')
        try:
            # Добавление ссылки в общий списокок ссылок
            list_links.append(href.get('href'))
        except:
            pass

# Парсинг полученных ссылок с главной страницы
for link in list_links:

    # Составление url для главного документа
    common_url = short_link + link
    #  Получение html страницы документа
    html_doc = get_html(common_url)
    # Парсинг страницы
    bs = BeautifulSoup(html_doc, 'html.parser')
    
    # Находим теги td с определенным классом
    for item in bs.find_all('td', class_ = 'noticeTdFirst fontBoldTextTd'):

        # Создание пустого словаря для того, чтобы добавлять полученные данные
        dct = {}
        try:
            # Проверка найденного значения среди необходимых полей
            if item.text.strip() in keys_44fz:
                # Текст внутри необходимого тега
                info = item.find_next_sibling('td')
                # Добавление в словарь ключа и значени
                dct[item.text.strip()] = info.text.strip()
                # Добавляем в список полученный словарь
                list_dct.append(dct)
        except AttributeError:
            pass

print(list_dct)

# ---------------------------------------------------------------------------

# http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html?pageNumber=1&recordsPerPage=_50&fz44=on&fz223=on&ppRf615=on&af=on&ca=on&pc=on&pa=on&priceFromGeneral=1111111111&priceToGeneral=22222222222&updateDateFrom=18.10.2018&updateDateTo=18.10.2018
# Составляем переменные url, чтобы составить правильный запрос
# af=on - подача заявок
# ca=on - работа комиссии
# pc=on - процедура завершена
# pa=on - процедура отменена
# priceFromGeneral - minimum price
# priceToGeneral - max price
# params = {
#         'pageNumber': 1,
#         'recordsPerPage': '_50',
#         'fz44': 'on',
#         'fz223': 'off',
#         'ppRf615': 'off',
#         'af': 'off',
#         'ca': 'off',
#         'pc': 'on', 
#         'pa': 'off',
#         'updateDateFrom': dt_now.strftime('%d.%m.%Y'),
#         'updateDateTo': dt_now.strftime('%d.%m.%Y'),
#         'priceFromGeneral': '1000000',
#         'priceToGeneral': '2222222222'
# }



http://www.zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html?regNumber=0361200015018006321
http://www.zakupki.gov.ru/epz/order/notice/ea44/view/documents.html?regNumber=0361200015018006321
http://www.zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html?regNumber=0361200015018006321


http://www.zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html       ?regNumber=0334300027618000126
http://www.zakupki.gov.ru/epz/order/notice/ea44/view/documents.html         ?regNumber=0334300027618000126
http://www.zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html  ?regNumber=0334300027618000126
http://www.zakupki.gov.ru/epz/order/notice/ea44/view/event-journal.html     ?regNumber=0334300027618000126
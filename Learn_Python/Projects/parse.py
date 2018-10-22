from bs4 import BeautifulSoup
# Работа с датой, нужно чтобы получать дату здесь и сейчас
from datetime import datetime
# Импорт функции, которая находится в req, для того, чтобы получить html сайта
from req import get_html

# html посковой страницы сайта госзакупки
search_html = 'http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html'
# Переменная хранит дату сегодняшнего дня
dt_now = datetime.now()
dt_now = '22.10.2018'
# Начало ссылки, нужна для того, чтобы перейти к документу
short_link = 'http://www.zakupki.gov.ru'
# Вкладки документа по ФЗ44
tab_fz44 = ['common-info', 'documents', 'supplier-results', 'event-journal']
# Переменная будет хранить все нужные ссылки на документы
list_links = []
# Общий словарь всех нужных данных
list_dct = []
# Переменная будет хранить id каждой новой закупки
dct_id = {}
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
# Тестовые параметры для парсинга поисковой выдачи
test_params = {
    'pageNumber': 1,
    'recordsPerPage': '_50',
    'fz44': 'on',
    'pc': 'on',
    # 'updateDateFrom': dt_now.strftime('%d.%m.%Y'),
    # 'updateDateTo': dt_now.strftime('%d.%m.%Y'),
    'updateDateFrom': dt_now,
    'updateDateTo': dt_now,
    'priceFromGeneral': '100000000',
    'priceToGeneral': '1000000000'
}

# Функция парсинга подразделов документа


def parsing_main_goc(url, tag, class_tag, keys, list_dct=list_dct, dop_tag='a'):
    """ 
        Функция принимает url, значения искомого тега, класса, список нужных 
        ключей, список куда будут складываться словари и дополнительный тег, 
        если нужно будет парсить внутри найденого текста.
    """

    #  Получение html страницы документа
    html = get_html(url)
    # Парсинг страницы
    bs = BeautifulSoup(html, 'html.parser')

    # Находим тег с определенным классом
    for item in bs.find_all(tag, class_=class_tag):

        # Создание пустого словаря для того, чтобы добавлять полученные данные
        dct = {}
        try:
            # Проверка найденного значения среди необходимых полей
            if item.text.strip() in keys:
                # Текст внутри необходимого тега
                info = item.find_next_sibling(tag)
                # Добавление в словарь ключ и значени
                dct[item.text.strip()] = info.text.strip()
                # Добавляем в список полученный словарь
                list_dct.append(dct)
        except AttributeError:
            pass

# Функция вытягвает название документов и их ссылки
def parsing_link_doc(url, tag, class_tag, list_dct=list_dct, dop_tag='a'):
    """
    """
    # Временный список, для хранения словарей
    list_links = []
    # Временныфй словарь со списком ссылок
    dct_link = {}

    html = get_html(url)
    bs = BeautifulSoup(html, 'html.parser')

    # Проходим циклом и вытягиваем ссылки на тендеры
    for item in bs.find_all(tag, class_tag):
        # Словарь для добавления (временный)
        dct = {}
        # Временный список, для хранения словарей
        list_links = []
        try:
            # Получение ссылок
            href_title = item.find(dop_tag)         # Исправить на find_all и узнать как пройти по ним циклом, чтобы вытягивать нужные документы - нужны не все ссылки
            # Получаем title(key) and link(value)
            dct[href_title.get('title')] = href_title.get('href')
            # Добавляем словарь в список
            list_links.append(dct)
        except:
            pass
    
    # Добавляем полученный список в еще один словарь
    dct_link['Извещение, документация об электронном аукционе'] = list_links
    # Добавляем этот словарь в общий список
    list_dct.append(dct_link)


# Запуск парсинга страницы поиска с необходимыми значения
for item in range(1, 20):

    # Добавляем следующую страницу для парсинга
    test_params['pageNumber'] = item
    html = get_html(search_html, params=test_params)
    # Парсим страницу
    bs = BeautifulSoup(html, 'html.parser')

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
    # Отделяем id от ссылки
    id_purchase = link.split('=')
    # Добавляем в словарь id закупки
    dct_id['id'] = id_purchase[1]
    # Добавляем это значение в список словарей
    list_dct.append(dct_id)
    # Запускаем функция для парсинга документа на главной странице
    parsing_main_goc(common_url, 'td', 'noticeTdFirst fontBoldTextTd', keys_44fz, list_dct)
    # Меняем url документа на следующюю вкладку
    common_url = common_url.replace(tab_fz44[0], tab_fz44[1])
    print(common_url)
    # Парсим следующую вкладку документа
    parsing_link_doc(common_url, 'div', 'displayTable', list_dct, 'a')


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


# fz44
# http://www.zakupki.gov.ru/epz/order/notice/ea44/view/common-info.html       ?regNumber=0334300027618000126
# http://www.zakupki.gov.ru/epz/order/notice/ea44/view/documents.html         ?regNumber=0334300027618000126
# http://www.zakupki.gov.ru/epz/order/notice/ea44/view/supplier-results.html  ?regNumber=0334300027618000126
# http://www.zakupki.gov.ru/epz/order/notice/ea44/view/event-journal.html     ?regNumber=0334300027618000126

# Основная задача этого скрипка - наполнение данные таблицы Zakupki44. 
# Данные берутся из основной таблицы, выбираем поля, которые по 44 закоку,
# парсим страницу документа и складываем данные в таблицу


from bs4 import BeautifulSoup
import sqlite3
import sqlalchemy
# Работа с датой, нужно чтобы получать дату здесь и сейчас
from datetime import datetime
# Импорт функции, которая находится в req, для того, чтобы получить html сайта
from req import get_html
# Импортируем base_table.db для того, чтобы добавлять данные с гланой страницы
from base_table import db_session, BaseZakupki
from table44 import db_session, Zakupki44

# Список в котором будут хранится данные для таблицы
list_data = []
# Все поля из основной БД по 44-ФЗ
all_data = BaseZakupki.query.filter(BaseZakupki.number_fz == 44).all()

# html страницы 44 закона 
http_common = 'http://www.zakupki.gov.ru/epz/order/notice/ep44/view/{}.html'\
                '?regNumber={}'
# Вкладки документа по ФЗ44
tab_fz44 = ['common-info', 'documents', 'supplier-results', 'event-journal']
# Ключи по которым ищем данные на странице
keys_44fz = [
    'Способ определения поставщика (подрядчика, исполнителя)',
    'Размещение осуществляет',
    'Начальная (максимальная) цена контракта',
    'Место доставки товара, выполнения работы или оказания услуги',
    'Дата выполнения контракта',
    'Размер обеспечения исполнения контракта',
    """Сроки поставки товара или завершения работы либо
                график оказания услуг"""
]
# Если в документе есть это, то нам не интересен такой контракт
key_break = 'Обеспечение исполнения контракта не требуется'


# Функция для замены длинного ключа на короткий
def change_key(key):
    new_key = 'Дата выполнения контракта'
    if key == """Сроки поставки товара или завершения работы либо
                график оказания услуг""":
        return new_key
    else:
        return key


# Функция на проверку обеспечения исполнения контратка 
def contract_cool(url):
    #  Получение html страницы документа
    html = get_html(url)
    # Парсинг страницы
    bs = BeautifulSoup(html, 'html.parser')

    # Находим тег с определенным классом
    for item in bs.find_all('td', class_='noticeTdFirst fontBoldTextTd'):
        # Проверка заголовка
        if item.text.strip() == key_break:
            return False

    return True

# Функция парсинга первой вкладки документа
def parsing_main_doc(url, tag, class_tag, keys, list_dct):
    """ 
        Функция принимает url, значения искомого тега, класса, список нужных 
        ключей, список куда будут складываться данные
    """

    #  Получение html страницы документа
    html = get_html(url)
    # Парсинг страницы
    bs = BeautifulSoup(html, 'html.parser')
    # Добавляем ключи словарей в список для проверки
    list_keys = []

    # Находим тег с определенным классом
    for item in bs.find_all(tag, class_=class_tag):

        # Создание пустого словаря для того, чтобы добавлять полученные данные
        dct = {}
        try:
            # Проверка найденного значения среди необходимых полей
            if item.text.strip() in keys and not item.text.strip() in list_keys:
                    # Добавляем в список ключей ключ словаря
                    list_keys.append(item.text.strip())
                    # Текст внутри необходимого тега
                    info = item.find_next_sibling(tag)
                    # Добавление в словарь ключ и значени и меняем ключ если чё
                    dct[change_key(item.text.strip())] = info.text.strip()
                    # Добавляем в список найденные данные
                    list_dct.append(dct)
        except AttributeError:
            pass

# Функция для добавления данных в БД
def add_data_bd(bd_session, list_dct=[], keys=[]):
    data = Zakupki44(list_dct[0]['id'],
                     list_dct[1][keys[0]],
                     list_dct[2][keys[1]],
                     list_dct[3][keys[2]],
                     list_dct[4][keys[3]],
                     list_dct[5][keys[4]],
                     list_dct[6][keys[5]],
                     list_dct[7],
                     list_dct[8],
                     list_dct[9])
    db_session.add(data)


# Запускаем в цикле каждую строчку для 44-ФЗ
for item in all_data:

    # Очищаем список перед каждым запуском цикла
    list_data = []
    # Словарь для добавления в список
    dct = {}

    # Проверяем есть ли такой id в таблице для 44-ФЗ
    if Zakupki44.query.filter(Zakupki44.id_zakupki == item.id_zakupki).first():
        continue
    elif contract_cool(http_common.format(tab_fz44[0], item.id_zakupki)):
        # Добавили id в список
        dct['id'] = item.id_zakupki
        list_data.append(dct)

        # Составляем url по каждой вкладки
        for tab in tab_fz44:

            url = http_common.format(tab, item.id_zakupki)
            # Если это первая вкладка, то парсим ее полностью, оcтальные нет
            if tab == 'common-info':
                try:
                    # Запускаем парсинг, поиск данных и добавление их
                    parsing_main_doc(url, 'td', 
                    'noticeTdFirst fontBoldTextTd', keys_44fz, list_data)
                except:
                    pass
            else:
                list_data.append(url)
    # Проверка списка на пустотность и на длину
    if list_data and len(list_data) == 10:
        # Добавление данных в таблицу
        add_data_bd(db_session, list_data, keys_44fz)

# Коммитим данные в БД
db_session.commit()


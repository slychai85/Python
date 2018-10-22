from bs4 import BeautifulSoup
from req import get_html

# Тестовый вариант парсинга вкладки документы, где надо вытащить ссылки на 
# документы и title

# Список для хранения нужных документов
list_links = []

html_test = get_html('http://www.zakupki.gov.ru/epz/order/notice/ea44/view/documents.html?regNumber=0366300002118000060')
bs = BeautifulSoup(html_test, 'html.parser')

# Проходим циклом и вытягиваем ссылки на тендеры
for item in bs.find_all('div', class_='displayTable'):
    # Словарь для добавления (временный)
    dct = {}
    try:
         # Получение ссылок
        href_title = item.find('a')
        # Получаем title(key) and link(value)
        dct[href_title.get('title')] = href_title.get('href')
        # Добавляем словарь в список
        list_links.append(dct)
    except:
        pass

print(list_links)
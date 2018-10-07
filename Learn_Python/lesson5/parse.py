from bs4 import BeautifulSoup
from req import get_html

html = get_html('http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html?morphology=on&pageNumber=1&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false&fz44=on&pc=true&currencyIdGeneral=-1&updateDateFrom=03.10.2018&updateDateTo=03.10.2018&regionDeleted=false&sortBy=UPDATE_DATE&openMode=USE_DEFAULT_PARAMS')


bs = BeautifulSoup(html, 'html.parser')


# print(bs.prettify())

# for item in bs.find_all('td', class_='tenderTd'):
#     print(item.text)

# for item in bs.find_all('td', { 'class' : 'descriptTenderTd ', 'class' : 'tenderTd'} ):
#     print(item.text)

# Получаем все данные по классам {} все вместе это 
# for item in bs.find_all(True, { 'class' : ['descriptTenderTd', 'tenderTd', 'amountTenderTd']} ):
#     print(item.text)

for item in bs.find_all('tbody'):
    print(item.text)

# http://www.zakupki.gov.ru/epz/main/public/home.html
# http://www.zakupki.gov.ru/epz/order/extendedsearch/results.html?morphology=on&pageNumber=1&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false&fz44=on&pc=true&currencyIdGeneral=-1&updateDateFrom=03.10.2018&updateDateTo=03.10.2018&regionDeleted=false&sortBy=UPDATE_DATE&openMode=USE_DEFAULT_PARAMS
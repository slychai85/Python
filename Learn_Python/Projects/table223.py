from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Выбор базы данных и название файла для его создания
engine = create_engine('sqlite:///table223.db')

# Сессия работы с БД - соединение с БД - bind -> привязаться
db_session = scoped_session(sessionmaker(bind=engine))

# Класс для sqlalchemy
Base = declarative_base()
Base.query = db_session.query_property()


# Описание таблицы
# Создание класса User, который наследуется от Base
class Zakupki223(Base):

    # Таблица для ФЗ-223
    __tablename__ = 'zakupki223'
    id = Column(Integer, primary_key=True)
    # id закупки
    id_zakupki = Column(Integer, unique=True)
    # Способ размещения закупки
    provider = Column(String(150))
    # Наименование закупки
    name_purchase = Column(String(500))
    # Наименование организации
    name_organization = Column(String(500))
    # Начальная (максимальная) цена контракта (можно вытянуть по  
    # <tr class='odd'> <td>...Российский рубль</td>) Находится в другой вкладке
    price = Column(String(50))
    # Ссылки на вкладку Документы
    doc_link = Column(String(100))
    # Ссылка на вкладку Протоколы
    protocol_link = Column(String(100))

    # Метод класса для добавления новых данных в таблицу по полям
    def __init__ (self, id_zakupki=None,
                        provider=None,
                        name_purchase=None,
                        name_organization=None,
                        price=None,
                        doc_link=None,
                        protocol_link=None):
        self.id_zakupki = id_zakupki
        self.provider = provider
        self.name_purchase = name_purchase
        self.name_organization = name_organization
        self.price = price
        self.doc_link = doc_link
        self.protocol_link = protocol_link

    # Способ вывода данных
    def __repr__(self):
        return '<BaseZakupki {} {} {} {} {} {} {}>'.format(
                self.id_zakupki, 
                self.provider,
                self.name_purchase,
                self.name_organization,
                self.price,
                self.doc_link,
                self.protocol_link)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
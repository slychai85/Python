from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Выбор базы данных и название файла для его создания
engine = create_engine('sqlite:///table44.sqlite')

# Сессия работы с БД - соединение с БД - bind -> привязаться
db_session = scoped_session(sessionmaker(bind=engine))

# Класс для sqlalchemy
Base = declarative_base()
Base.query = db_session.query_property()


# Описание таблицы
# Создание класса User, который наследуется от Base
class Zakupki44(Base):

    # Таблица для ФЗ-44
    __tablename__ = 'zakupki44'
    id = Column(Integer, primary_key=True)
    # id закупки
    id_zakupki = Column(String(30), unique=True)
    # Способ определения поставщика (подрядчика, исполнителя)
    provider = Column(String(550))
    # Размещение осуществляет
    customer = Column(String(500))
    # Начальная (максимальная) цена контракта
    price = Column(String(200))
    # Место доставки товара, выполнения работы или оказания услуги
    area = Column(String(500))
    # Дата выполнения контракта
    finish_date = Column(String(500))
    # Размер обеспечения исполнения контракта
    contract = Column(String(500))
    # Ссылки на вкладку Документы
    doc_link = Column(String(200))
    # Ссылка на вкладку Результаты определения поставщика
    result_link = Column(String(200))
    # Ссылка на вкладку Журнал событий 
    event_log_link = Column(String(200))

    # Метод класса для добавления новых данных в таблицу по полям
    def __init__ (self, id_zakupki=None,
                        provider=None,
                        customer=None,
                        price=None,
                        area=None,
                        finish_date=None,
                        contract=None,
                        doc_link=None,
                        result_link=None,
                        event_log_link=None):
        self.id_zakupki = id_zakupki
        self.provider = provider
        self.customer = customer
        self.price = price
        self.area = area
        self.finish_date = finish_date
        self.contract = contract
        self.doc_link = doc_link
        self.result_link = result_link
        self.event_log_link = event_log_link

    # Способ вывода данных
    def __repr__(self):
        return '<BaseZakupki {} {} {} {} {} {} {} {} {} {}>'.format(
                self.id_zakupki, 
                self.provider,
                self.customer,
                self.price,
                self.area,
                self.finish_date,
                self.contract,
                self.doc_link,
                self.result_link,
                self.event_log_link)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
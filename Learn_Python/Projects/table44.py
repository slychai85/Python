from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Выбор базы данных и название файла для его создания
engine = create_engine('sqlite:///table44.db')

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
    id_zakupki = Column(Integer, unique=True)
    # Способ определения поставщика (подрядчика, исполнителя)
    provider = Column(String(150))
    # Размещение осуществляет
    customer = Column(String(500))
    # Сведения о связи с позицией плана-графика
    order_plan = Column(String(200))
    # Начальная (максимальная) цена контракта
    price = Column(String(50))
    # Место доставки товара, выполнения работы или оказания услуги
    area = Column(String(300))
    # Сроки поставки товара или завершения работы либо график оказания услуг
    period = Column(String(100))
    # Размер обеспечения исполнения контракта
    contract = Column(String(100))
    # Ссылки на вкладку Документы
    doc_link = Column(String(100))
    # Ссылка на вкладку Результаты определения поставщика
    result_link = Column(String(100))
    # Ссылка на вкладку Журнал событий 
    event_log_link = Column(String(100))

    # Метод класса для добавления новых данных в таблицу по полям
    def __init__ (self, id_zakupki=None,
                        provider=None,
                        customer=None,
                        order_plan=None,
                        price=None,
                        area=None,
                        period=None,
                        contract=None,
                        doc_link=None,
                        result_link=None,
                        event_log_link=None):
        self.id_zakupki = id_zakupki
        self.provider = provider
        self.customer = customer
        self.order_plan = order_plan
        self.price = price
        self.area = area
        self.period = period
        self.contract = contract
        self.doc_link = doc_link
        self.result_link = result_link
        self.event_log_link = event_log_link

    # Способ вывода данных
    def __repr__(self):
        return '<BaseZakupki {} {} {} {} {} {} {} {} {} {} {}>'.format(
                self.id_zakupki, 
                self.provider,
                self.customer,
                self.order_plan,
                self.price,
                self.area,
                self.period,
                self.contract,
                self.doc_link,
                self.result_link,
                self.event_log_link)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
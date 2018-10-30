from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Выбор базы данных и название файла для его создания
engine = create_engine('sqlite:///base_table.db')

# Сессия работы с БД - соединение с БД - bind -> привязаться
db_session = scoped_session(sessionmaker(bind=engine))

# Класс для sqlalchemy
Base = declarative_base()
Base.query = db_session.query_property()


# Описание таблицы
# Создание класса User, который наследуется от Base
class BaseZakupki(Base):

    # Общая таблица для хранения id закупок и законов
    __tablename__ = 'base_zakupki'
    id = Column(Integer, primary_key=True)
    # id закупки
    id_zakupki = Column(Integer, unique=True)
    # Номер закона
    number_fz = Column(Integer)
    # Дата + время добавления в базу
    date_time = Column(String(30))

    # Метод класса для добавления новых данных в таблицу по полям
    def __init__(self, id_zakupki=None, number_fz=None, date_time=None):
        self.id_zakupki = id_zakupki
        self.number_fz = number_fz
        self.date_time = date_time

    def __repr__(self):
        return '<BaseZakupki {} {} {}>'.format(self.id_zakupki, self.number_fz, self.date_time)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Выбор базы данных и название файла для его создания
engine = create_engine('sqlite:///table_users.sqlite')

# Сессия работы с БД - соединение с БД - bind -> привязаться
db_session = scoped_session(sessionmaker(bind=engine))

# Класс для sqlalchemy
Base = declarative_base()
Base.query = db_session.query_property()


# Описание таблицы
# Создание класса User, который наследуется от Base
class User(Base):

    # Таблица для пользователей
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    # email адрес пользователя
    email = Column(String(120), unique=True)
   

    # Метод класса для добавления новых данных в таблицу по полям
    def __init__ (self, email=None):
        self.email = email

    # Способ вывода данных
    def __repr__(self):
        return self.email


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

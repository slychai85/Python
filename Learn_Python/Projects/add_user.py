from table_users import db_session, User
import sqlalchemy

me = User(email='')
db_session.add(me)
db_session.commit()

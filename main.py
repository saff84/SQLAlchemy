import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from tables import create_tables



DSN = 'postgresql://postgres:310884@localhost:5432/book_shop_db'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()
pub = input('Введите идентификатор издателя')

q = session.query(Publisher).filter(Publisher.name == pub)
print(q)

session.close()
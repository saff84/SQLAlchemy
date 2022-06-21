import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from tables import create_tables, Publisher, Book, Shop, Stock, Sale



DSN = 'postgresql://postgres:310884@localhost:5432/book_shop_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_items_from_test():
    with open('test_data.json', 'r') as data:
        data_data = json.load(data)
        for el in data_data:
            print(el)
            if el['model'] == "publisher":
                pub = Publisher(name = el['fields']['name'])
                session.add(pub)
                session.commit()
            elif el['model'] == "book":
                bk = Book(title=el['fields']['title'], publisher = int(el['fields']['publisher']))
                session.add(bk)
                session.commit()
            elif el['model'] == "shop":
                sh = Shop( name = el['fields']['name'])
                session.add(sh)
                session.commit()
            elif el['model'] == "stock":
                st = Stock( shop = el['fields']['shop'],book = el['fields']['book'],count = int(el['fields']['count']))
                session.add(st)
                session.commit()
            elif el['model'] == "sale":
                sal = Sale(price=el['fields']['price'],date_sale=el['fields']['date_sale'],count=int(el['fields']['count']),stock=int(el['fields']['stock']))
                session.add(sal)
                session.commit()


add_items_from_test()
session.close()
# pub = input('Введите Название издателя: ')
#
# q = session.query(Publisher).filter(Publisher.name == pub)
# print(q)
#
# session.close()
import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from tables import create_tables, Publisher, Book, Shop, Stock, Sale


DSN = 'postgresql://postgres:??????????@localhost:5432/book_shop_db' # пароль нужен
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_items_from_test():
    with open('test_data.json', 'r') as data:
        data_data = json.load(data)
        for el in data_data:

            if el['model'] == "publisher":
                pub = Publisher(name=el['fields']['name'])
                session.add(pub)
                session.commit()
            elif el['model'] == "book":
                bk = Book(
                    title=el['fields']['title'],
                    id_publisher=el['fields']['publisher'])
                session.add(bk)
                session.commit()
            elif el['model'] == "shop":
                sh = Shop(name=el['fields']['name'])
                session.add(sh)
                session.commit()
            elif el['model'] == "stock":
                st = Stock(
                    id_shop=el['fields']['shop'],
                    id_book=el['fields']['book'])
                session.add(st)
                session.commit()
            elif el['model'] == "sale":
                sal = Sale(
                    price=el['fields']['price'],
                    data_sale=el['fields']['date_sale'],
                    count=el['fields']['count'],
                    id_stock=el['fields']['stock'])
                session.add(sal)
                session.commit()


add_items_from_test()

pub = input('Введите Название издателя: ')


q = session.query(Publisher).filter(Publisher.name.like(f'%{pub}%'))

for p in q.all():
    print(p.id, p.name)


session.close()

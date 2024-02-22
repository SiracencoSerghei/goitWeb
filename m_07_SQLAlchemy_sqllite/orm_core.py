from sqlalchemy import (MetaData, create_engine, Table,
                        Column, Integer, String, ForeignKey)
from sqlalchemy.sql import select


engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('email_address', String, nullable=False),
    Column('user_id', Integer, ForeignKey('users.id')),
)

metadata.create_all(engine)

if __name__ == '__main__':
    with engine.connect() as conn:
        ins_user = users.insert().values(name='jack', fullname='Jack Jones')
        print("1  ", str(ins_user))
        print("2  ", ins_user)
        result = conn.execute(ins_user)
        jones_id = result.lastrowid
        print("jones_id :  ",jones_id)
        # print(result)
        # print(dir(result))

        ins_user = users.insert().values(name='sergio', fullname='Sergio Tacchini')
        result = conn.execute(ins_user)
        tacchini_id = result.lastrowid
        print("tacchini_id :  ", tacchini_id)
        ins_user = users.insert().values(name='pietro', fullname='San Pietro')
        result = conn.execute(ins_user)
        pietro_id = result.lastrowid
        print("pietro_id :  ", pietro_id)

        # ========================
        ins_address = addresses.insert().values(email_address='jackjones@example.com', user_id=jones_id)
        result = conn.execute(ins_address)
        ins_address = addresses.insert().values(email_address='sergiotacchini@example.com', user_id=tacchini_id)
        result = conn.execute(ins_address)
        ins_address = addresses.insert().values(email_address='sanpietro@example.com', user_id=pietro_id)
        result = conn.execute(ins_address)

        s = select(users)
        result = conn.execute(s)
        for row in result:
            print(row)  # (1, u'jack', u'Jack Jones')

        s = select(addresses)
        result = conn.execute(s)
        for row in result:
            print(row)

        result = conn.execute(select(users.c.id, users.c.fullname, addresses.c.email_address).join(users))
        for row in result:
            print(row)

        #  if not with construction:  with engine.connect() as conn:
        # need to close....
        # engine.connect().commit()

import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, text
from sqlalchemy import create_engine

def create_tables(metadata):
    users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String),
    )

    addresses = Table('addresses', metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey('users.id')),
        Column('email_address', String, nullable=False)
    )

    return users, addresses


def execute_con(conn, cmd):
    print("-------------------------")
    result = conn.execute(cmd)

    try:
        for raw in result:
            print(raw)
    except sqlalchemy.exc.ResourceClosedError as e:
        pass
    finally:
        print("-------------------------")


def main(engine):
    metadata = MetaData()
    # create tables
    users, addresses = create_tables(metadata)

    print("Tables:")
    for t in metadata.sorted_tables:
        print(t.name)
    print("----------------------------")

    metadata.create_all(engine)

    ins = users.insert().values(name='Sergio', fullname='Sergio Tacchini')
    print(ins)

    # dlt = users.delete().where(
    #     sqlalchemy.and_(
    #         users.c.name == 'Sergio',
    #         users.c.fullname == 'Sergio Tacchini'
    #     )
    # )
    # print(dlt)

    slt = users.select()
    print(slt)

    with engine.connect() as conn:
        execute_con(conn, ins)
        execute_con(conn, slt)
        # execute_con(conn, dlt)
        execute_con(conn, slt)
        
          
        
    # engine.connect().execute(slt)
    # with engine.connect() as conn:
    #     result = conn.execute(text("select 'hello world'"))
    #     print(result.all())

if __name__ == "__main__":
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
    main(engine)

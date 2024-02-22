from models import db, Groups, Students, Teachers, Subjects, Grages
from seed_db import populate_db
from db_operations import task_7, top_5_students_by_subject

def create_tables():
    try:
        db.connect()
        db.create_tables([Groups, Students, Teachers, Subjects, Grages], safe=True)
    except Exception as e:
        print(e)
    finally:
        db.close()


if __name__ == '__main__':
    # create_tables()
    # populate_db()

    # task_7()
    top_5_students_by_subject(1)
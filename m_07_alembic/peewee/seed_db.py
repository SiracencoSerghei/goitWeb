from models import db, Groups, Students, Teachers, Subjects, Grages
from faker import Faker
import random


faker = Faker()
group_names = ["Group_A", "Group_B", "Group_C"]


def populate_db():
    try:
        db.connect()

        teachers_list = []
        subjects_list = []
        groups_list = []
        students_list = []

        for _ in range(5):
            teachers = Teachers.create(name_teacher=faker.name())
            teachers_list.append(teachers)
        for i in range(1, 9):
            subjects = Subjects.create(name_subject=f"Subj_{i}", teachers=random.choice(teachers_list))
            subjects_list.append(subjects)
        for i in range(3):
            groups = Groups.create(group_name=f"{group_names[i]}")
            groups_list.append(groups)
        for _ in range(50):
            students = Students.create(student_name=faker.name(), group=random.choice(groups_list))
            students_list.append(students)
        for _ in range(200):
            grades = Grages.create(
                score=random.randint(50, 100),
                students=random.choice(students_list),
                subjects=random.choice(subjects_list),
                score_date=faker.date_between(start_date="-1y", end_date="today")
            )
        print("DataBase populated...")
    except Exception as e:
        print(e)
    finally:
        db.close()





from peewee import *
from dotenv import dotenv_values


config = dotenv_values(".env")

db = PostgresqlDatabase(
    config['POSTGRES_DB'],
    user=config['POSTGRES_USER'],
    password=config['POSTGRES_PASSWORD'],
    host=config['POSTGRES_HOST'],
    port=config['POSTGRES_PORT']
)


class BaseModel(Model):
    class Meta:
        database = db


class Teachers(BaseModel):
    name_teacher = CharField()

    class Meta:
        table_name = "teachers"


class Subjects(BaseModel):
    name_subject = CharField()
    teachers = ForeignKeyField(Teachers, backref="subjects")

    class Meta:
        table_name = "subjects"


class Groups(BaseModel):
    group_name = CharField()

    class Meta:
        table_name = "groups"


class Students(BaseModel):
    student_name = CharField()
    group = ForeignKeyField(Groups, backref="students")

    class Meta:
        table_name = "students"


class Grages(BaseModel):
    score = IntegerField()
    score_date = DateField()
    students = ForeignKeyField(Students, backref="grades")
    subjects = ForeignKeyField(Subjects, backref="grades")

    class Meta:
        table_name = "grades"

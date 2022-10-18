from configs import *
from peewee import *


db = SqliteDatabase('db/database.db')


class BaseModel(Model):
    class Meta:
        database = db


class QuizAnswer(BaseModel):
    id = AutoField()
    question_id = IntegerField()
    answer = CharField(max_length=MAX_ANSWER_LENGTH)
    correct = BooleanField()


class QuizQuestion(BaseModel):
    id = AutoField()
    theme_id = IntegerField()
    weight = IntegerField()
    question = CharField(max_length=MAX_QUESTION_LENGTH)


class QuizTheme(BaseModel):
    id = AutoField()
    quiz_id = IntegerField()
    text = CharField(max_length=MAX_THEME_LENGTH)


class QuizInfo(BaseModel):
    id = AutoField()
    title = CharField(max_length=MAX_TITLE_LENGTH)

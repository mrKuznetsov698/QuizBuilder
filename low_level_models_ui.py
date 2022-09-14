from typing import List
from models import QuizQuestion, QuizTheme, QuizInfo, QuizAnswer


def create_databases():
    QuizAnswer.create_table()
    QuizQuestion.create_table()
    QuizTheme.create_table()
    QuizInfo.create_table()


def create_answer(question_id: int, answer: str, correct: bool) -> QuizAnswer:
    return QuizAnswer.create(question_id=question_id,
                             answer=answer,
                             correct=correct)


def create_question(theme_id: int, weight: int, question: str) -> QuizQuestion:
    return QuizQuestion.create(theme_id=theme_id,
                               weight=weight,
                               question=question)


def create_theme(quiz_id: int, text: str) -> QuizTheme:
    return QuizTheme.create(quiz_id=quiz_id,
                            text=text)


def create_quiz(title: str) -> QuizInfo:
    return QuizInfo.create(title=title)


def get_all_answers() -> List[QuizAnswer]:
    return list(QuizAnswer.select())


def get_all_questions() -> List[QuizQuestion]:
    return list(QuizQuestion.select())


def get_all_themes() -> List[QuizTheme]:
    return list(QuizTheme.select())


def get_all_info() -> List[QuizInfo]:
    return list(QuizInfo.select())


def get_answers_by_question_id(question_id: int) -> List[QuizAnswer]:
    return list(QuizAnswer.select().where(QuizAnswer.question_id == question_id))


def get_questions_by_theme_id(theme_id: int) -> List[QuizQuestion]:
    return list(QuizQuestion.select().where(QuizQuestion.theme_id == theme_id))


def get_themes_by_quiz_id(quiz_id: int) -> List[QuizTheme]:
    return list(QuizTheme.select().where(QuizTheme.quiz_id == quiz_id))


def get_quiz_info(id: int) -> QuizInfo:
    return list(QuizInfo.select().where(QuizInfo.id == id))[0]

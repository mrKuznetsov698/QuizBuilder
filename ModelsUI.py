from models import QuizQuestion, QuizTheme, QuizInfo, QuizAnswer
from low_level_models_ui import *

r"""
    config = {
        "title": "Тест по математики",
        "themes": [
            {"name": "формулы", questions: [
                {"question": "2+2", "weight": 10, "answers": [
                    {"text": "4", "correct": true},
                    {"text": "3.(3)", "correct": false},
                    {"text": "5", "correct": false}
                ]},
                {"question": "4+2", "weight": 10, "answers": [
                    {"text": "6", "correct": true},
                    {"text": "21.(3)", "correct": false},
                    {"text": "19", "correct": false}
                ]}
            ]},
            {"name": "пуккек", questions: [
                {"question": "2+2", "weight": 10, "answers": [
                    {"text": "4", "correct": true},
                    {"text": "3.(3)", "correct": false},
                    {"text": "5", "correct": false}
                ]},
                {"question": "4+2", "weight": 10, "answers": [
                    {"text": "6", "correct": true},
                    {"text": "21.(3)", "correct": false},
                    {"text": "19", "correct": false}
                ]}
            ]},
        ],
    }
 """


def create_all_databases():
    create_databases()


def parse_config(config: dict):
    qi = create_quiz(config['title'])
    for theme in config['themes']:
        qt = create_theme(quiz_id=qi.id, text=theme['name'])
        for question in theme['questions']:
            qq = create_question(theme_id=qt.id, weight=question['weight'], question=question['question'])
            for answer in question['answers']:
                create_answer(question_id=qq.id, answer=answer['text'], correct=answer['correct'])

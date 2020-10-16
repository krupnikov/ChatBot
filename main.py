import random

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет', 'Здравствуйте', 'Добрый день'],
            'responses': []
        },
        'bye': {
            'examples': ['Bye-bye', 'До свидания', 'Увидимся'],
            'responses': ['Прощай', '']
        },
        'failure_phrase': [
            'Я не понял',
            'Перефразируйте, пожайлуста',
            'Мне не понятно',
            'Не умею отвечать на такое'
        ]
    }
}


def get_generative_answer():
    return 'Hello'  # TODO on 3th day


def get_intent(question):
    pass


def get_answer_by_intent(intent):
    phrases = [
        'Приветсвую',
        'Добрый день',
        'Добрый вечер',
        'Доброе утро'
    ]


def get_failure_phrase():
    phrases = BOT_CONFIG['failure_phrases']
    return random.choice(phrases)


# Easy bot function
def bot(question):
    #
    # NLU
    intent = get_intent(question)

    #
    # Answer from our intent list
    if intent:
        return get_answer_by_intent(intent)

    #
    # Generating model
    answer = get_generative_answer(question)
    if answer:
        return answer

    # Dummy answer
    return get_failure_phrase()

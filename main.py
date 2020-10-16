import random

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет', 'Здравствуйте', 'Добрый день'],
            'responses': ['Привет, человек', 'Здраствуйте!', 'Шалом']
        },
        'bye': {
            'examples': ['Bye-bye', 'До свидания', 'Увидимся'],
            'responses': ['Прощай', 'Приходи еще', 'Увидимся']
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
    return ''  # TODO on 3th day


def get_intent(question):
    for intent, intent_value in BOT_CONFIG['intents'].items():
        # print(intent, intent_value['examples'])
        for example in intent_value['examples']:
            # print(intent, example)
            if example == question:
                return intent
    return 'Hello'


def get_answer_by_intent(intent):
    phrases = BOT_CONFIG['intents'][intent]['responses']
    return random.choice(phrases)

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

print(bot(input(str())))
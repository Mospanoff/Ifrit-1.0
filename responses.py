class responses(object):
    hello_response_list = ["Доброго времени суток, сэр!",
                         "Приветствую,   сэр",
                         "Здравствуйте, сэр! Какие будут указания?"]

    goodbay_response_list = ["всего хорошего,    сэр",
                             "До свидания,    сэр",
                             "До скорого,   сэр",
                         "Хорошо провести время,    сэр"]
    
    confirmation_list = ["Сэр, Уточните пожалуйста",
                         "Сэр, можно по-конкретней",
                         "Сэр, Конкретизируйте пожалуйста"]

    micless_list = ['Удаляюсь, сэр!', 'Закрыл уши, сэр!', 'Глух, как пень!']

    quest_list = ["Как дела?", "Что нового?", "Как настроение?", "Что интересного?"]




def hello_response():
    from random import choice
    return choice(responses.hello_response_list)

def goodbay_response():
    from random import choice
    return choice(responses.goodbay_response_list)

def confirm_response():
    from random import choice
    return choice(responses.confirmation_list)

def micless_response():
    from random import choice
    return choice(responses.micless_list)

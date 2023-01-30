import controller


def input_trader():
    return input('Выберите барыгу :').upper()


def input_subject():
    print('Долги','\nВыплаты')
    return input('С чем работаем? :').lower()

def actor_name():
    return input('Кого посмотрим? :')


def what_summa():
    return input('Какую сумму записать?')


def list_of_actors(bd:dict):
    for i, actor in enumerate(bd,1):
        print(f'{i}.{actor:20} {bd.get(actor)}')
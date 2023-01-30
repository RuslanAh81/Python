import controller


def input_trader():
    return input('Выберите барыгу :').upper()

def main_menu():
    print('Меню:')
    for i, item in enumerate(commands,1):
        print(f'\t{i}.{item}')
    while True:
        try:
            choice =int(input('Выберите пункт меню: '))
            if 0<choice<5:
                return choice
            else:
                print('Введите значение от 1 до 4')
        except ValueError:
            print('Введите корректное значение')

# def input_subject():
#
#     return input('С чем работаем? :').lower()

def actor_name():
    return input('Кого посмотрим? :')


def what_summa():
    return input('Какую сумму записать?')


def list_of_actors(bd:dict):
    for i, actor in enumerate(bd,1):
        print(f'{i}.{actor:20} {bd.get(actor)}')


def input_error():
    print('Ошибка ввода.Введите корректный пункт меню')



commands = ['Выбрать должников',
            'Выплаты',
            'Добавить',
            'Выход из программы']
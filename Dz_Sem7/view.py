import model


def main_menu():
    print('Меню: ')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}.{item}')
    while True:
        try:
            choice=int(input('Выберите пункт меню: '))
            if 0 <choice<9:
                return choice
            else:
                print('Введите значение от 1 до 8')

        except ValueError:
            print('Введите корректное значение')



def show_contacts(phone_list:list):
    if len(phone_list)<1:
        print('Телефонная книга пуста')
    else:
        print()
        for i,contact in enumerate(phone_list, 1):
            print(f'\t{i}.{contact[0]:20}{contact[1]:13}{contact[2]:20}')
            print()

def create_new_contact():
    name = input('Введите имя и фамилию : ')
    phone= input('Введите номер телефона: ')
    comment= input('Введите комментарий: ')
    return name, phone, comment

def select_contact(message:str):
    contact= input(message)
    return contact

def change_contact():
    print('введите новые данные(Нажмите Enter): ')
    name = input('Введите имя и фамилию : ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def delete_confirm(contact:str):
    result = input(f'Вы действительно хотите удалить {contact}?(y/n)').lower()
    if result == 'y':
        return True
    else:
        return False

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def input_error():
    print('Ошибка ввода.Введите корректный пункт меню')

def empty_request():
    print('Искомый контакт не найден')

def many_request():
    print('Введите более точные данные.')

def end_programm():
    print('Досввидос')


commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']

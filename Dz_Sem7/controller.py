
import view
import model

def start():
    chice=''
    while True:
        choice=view.main_menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.show_contacts(model.get_phonebook())
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                del_name = view.select_contact('Введите удаляемый контакт: ')
                contact=model.get_contact(del_name)
                if contact:
                    confirm= view.delete_confirm(contact[0][0][0])
                    if confirm:
                        model.delete_contact(contact[0][0])
                elif contact ==[]:
                    view.empty_request()
                else:
                    view.many_request()

            case 6:
                name= view.select_contact('Введите изменяемый контакт: ')
                contact = model.get_contact(name)
                if contact:
                    changed_contact = view.change_contact()
                    model.change_contact(contact[0][1], list(changed_contact))
            case 7:
                find = view.find_contact()
                result= model.search_contact(find)
                view.show_contacts(result)
            case 8:
                view.end_programm()
                break
            case _:
                view.input_error()










import view
import model

def start():
    choice=''
    model.set_trader(view.input_trader())
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                bd = model.get_bd()
                view.list_of_actors(bd)
                # model.set_subject(view.input_subject())
                model.open_file()
                actor = ''
                actor = view.actor_name()
                summa = int(view.what_summa())
                model.actor_summa(actor, summa)

            case 2:
                model.add_new_actor()
            case 4:
                actor = 'exit'
                if actor == 'exit':
                    break


    model.save_file()
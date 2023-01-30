import view
import model

def start():
    model.set_trader(view.input_trader())
    model.set_subject(view.input_subject())
    model.open_file()
    actor = ''
    while True:
        bd = model.get_bd()
        view.list_of_actors(bd)
        actor = view.actor_name()
        if actor == 'exit':
            break
        summa = int(view.what_summa())
        model.actor_summa(actor, summa)

    model.save_file()


bd= {}
subject = ''
path=''

def set_trader(trader_path:str):
    global path
    path = trader_path +'.txt'

def set_subject(our_subject:str):
    global subject
    subject = our_subject


def open_file():
    with open(path, 'r', encoding='utf-8') as data:
        file = data.readlines()
    print(file)
    for sub in file:
        if sub.split(';')[0] == subject:
            for nps in sub.split(';')[1].strip().split(', '):
                bd[nps.split(':')[0]] = list(map(int, nps.split(':')[1].split()))


def add_new_actor(new_actor:str, summa):
    new_actor=[]




def save_file():
    new_file= []

    with open(path, 'r', encoding = 'utf-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for actors, summa in bd.items():
        item.append(actors + ':' + ' '.join(list(map(str, summa))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding = 'utf-8') as data:
        data.write('\n'.join(new_file))

def actor_summa(actor: str, summa):
    print(actor, summa)
    new_summa = list(bd.get(actor))
    new_summa.append(summa)
    bd[actor] = new_summa

def get_bd():
    return bd
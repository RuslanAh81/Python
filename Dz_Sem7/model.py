
phonebook = []

def get_phonebook():
    global phonebook
    return phonebook

def open_file():
    global phonebook
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        file = data.readlines()
        for contact in file:
            phonebook.append(contact.strip().split(';'))
        print(phonebook)

def save_file():
    global phonebook
    pb_str =[]
    for contact in phonebook:
        pb_str.append(';'.join(contact))
    with open('phonebook.txt','w', encoding='utf-8') as data:
        data.write('\n'.join(pb_str))



def add_new_contact(new_contact:list):
    global phonebook
    phonebook.append(new_contact)

def get_contact(text:str):
    global phonebook
    result = []
    for i, contact in enumerate(phonebook):
        for field in contact:
            if text in field:
                result.append((contact, i))
    if len(result) > 1:
        return False
    else:
        return result

def change_contact(index:int, new:list):
    phonebook[index][0]= new[0]if new[0] != '' else phonebook[index][0]
    phonebook[index][1]= new[1]if new[1] != '' else phonebook[index][1]
    phonebook[index][2]= new[2]if new[2] != '' else phonebook[index][2]

def search_contact(find:str):
    global phonebook
    result = []
    for contact in phonebook:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def delete_contact(contact:list):
    global phonebook
    phonebook.remove(contact)

from utils import input_error
from classes import AddressBook, Record, Notes, Note
from sort_files import sort_files

def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input) + 1:]
            break
    if data:
        data = data.split(' ')
        print(data)
        return reaction_func(new_input)(*data)
    return reaction_func(new_input)()

def stop():
    return 'Good bye!'

def greeting():
    return 'How can I help you?'

@input_error
def add_contact(name, phone):
    if name in address_book.data:
        return 'contact already exist'

    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return 'new contact added'

@input_error
def add_address(name, address):
    if name in address_book.data:
        record = address_book.data[name]
        record.add_address(address)
        return f'address "{address}" has been added to contact {name}'
    else:
        return 'contact does not exist'

@input_error
def add_phone(name, phone):
    if name in address_book.data:
        record = address_book.data[name]
        record.add_phone(phone)
        
        return f'a new phone "{phone}" has been added to contact {name}' 
    else:
        return 'contact does not exist'

@input_error
def add_email(name, email):
    if name in address_book.data:
        record = address_book.data[name]
        record.add_email(email)

        return f'a new email "{email}" has been added to contact {name}' 
    else:
        return 'contact does not exist'

@input_error
def add_birthday(name, birthday):
    if name in address_book.data:
        record = address_book.data[name]
        record.add_birthday(birthday)         
        return f'birthday {birthday} has been added to contact {name}'
    else:
        return 'contact does not exist' 

def show_all():
    if not address_book.data:
        return 'nothing to show'

    all_contacts = ''
  
    for name, record in address_book.items():
        phones_list = []
        for phone in record.phones:
            phones_list.append(phone.value)

        contact_info = f'{name} | phones: {phones_list} | '
        if record.birthday:
            contact_info += f'birthday: {record.birthday.value} | '
        if record.address:
            contact_info += f'address: {record.address.value} | '
        if record.email:
            contact_info += f'email: {record.email.value} | '
        
        all_contacts += f'{contact_info}\n'
        
    return all_contacts

@input_error
def add_note(title, *args):
    if args:
        title = f"{title} {' '.join(args)}"    

    if title in notes.data:
        return 'note with this name already exist'

    note = Note(title)
    note.text = input('Enter note text: ')
    notes.add_note(note)
    return 'new note added'

def show_notes():
    if not notes.data:
        return 'nothing to show'
    
    all_notes = '-------------------\n'

    for title, note in notes.items():
        all_notes += f'title: {title}\n'
        all_notes += f'text: {note.text}\n'
        all_notes += '-------------------\n'

    return all_notes

@input_error
def find_notes(words):
    if not notes.data:
        return 'nothing to show'

    finded_notes = '-------------------\n'

    for title, note in notes.items():
        if words in title or words in note.text:
            finded_notes += f'title: {title}\n'
            finded_notes += f'text: {note.text}\n'
            finded_notes += '-------------------\n'

    return finded_notes

@input_error
def change_note(title):
    if title in notes.data:
        note = notes.data[title]
        result = note.change_note(title)
        notes.add_note(note)
        
        if result == 'note title changed':
            delete_note(title)

        return result
    else:
        return 'note does not exist'

@input_error
def delete_note(title):
    if title in notes.data:
        del notes[title]
        return 'note deleted'
    else:
        return 'note does not exist'

def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_func)

def break_func():
    """
    Якщо користувач ввів якусь тарабарщину- повертаємо відповідну відповідь
    :return: Неправильна команда
    """
    return 'Wrong enter.'

COMMANDS_DICT = {
    'hello': greeting,
    'exit': stop,
    'close': stop,
    'add_contact': add_contact,
    'add_address': add_address, 
    'add_phone': add_phone,
    'add_email': add_email,
    'add_birthday': add_birthday,
    'show_all': show_all,
    'add_note': add_note,
    'show_notes': show_notes,
    'find_notes': find_notes,
    'sort_files': sort_files,
    'change_note': change_note,
    'delete_note': delete_note,
    # 'find_tag': find_tag,
}

def main():
    """
    Основна логика усього застосунку. Отримуємо ввід від користувача
    і відправляємо його в середину застосунку на обробку.
    :return:
    """
    while True:
        """
            Просимо користувача ввести команду для нашого бота
            Також тут же вимикаємо бота якщо було введено відповідну команду
       """

        user_input = input('Enter command for bot: ')
        result = change_input(user_input)
        print(result)
        if result == 'good bye':
            break

if __name__ == '__main__':
    address_book = AddressBook()
    notes = Notes()
    main()
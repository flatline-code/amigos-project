from utils import input_error
from classes import AddressBook, Record
from commands import COMMANDS_DICT

def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()

def stop():
    return 'Good bye!'

def greeting():
    return 'How can I help you?'

@input_error
def add_contact(name, phone):
    if name in adress_book.data:
        return 'contact already exist'

    record = Record(name)

    if not record.add_phone(phone):
        return 'something wrong with phone number'

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

        if not record.add_phone(phone):
            return 'something wrong with phone number'
        
        return f'a new phone "{phone}" has been added to contact {name}' 
    else:
        return 'contact does not exist'

@input_error
def add_email(name, email):
    if name in address_book.data:
        record = address_book.data[name]

        if not record.add_email(email):
            return 'something wrong with email'

        return f'a new email "{email}" has been added to contact {name}' 
    else:
        return 'contact does not exist'

@input_error
def add_birthday(name, birthday):
    if name in address_book.data:
        record = address_book.data[name]

        if not record.add_birthday(birthday):
            return 'birthday format must be dd.mm.yyyy'
            
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

def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_func)

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
    main()
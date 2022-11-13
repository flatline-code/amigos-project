from classes import AddressBook, Record

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
    }

def input_error(handler):
    def wrapper(*args):
        try:
            return handler(*args)
        except Exception as e:
            error_string = e.args[0] 
            print(error_string) 
            if 'add_address()' in error_string:
                return 'enter name and address'
            elif 'add_birthday()' in error_string:
                return 'enter name and birthday'
            elif 'add_email()' in error_string:
                return 'enter name and email'
            else:
                return 'enter name and phone' 
    return wrapper          
            
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
  
if __name__ == '__main__':
    address_book = AddressBook()
    main()
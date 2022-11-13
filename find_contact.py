#TODO to make a seperate file for constantcs/commands = import constants
#TODO to add utils for @input_error
#TODO to add class AddressBook


constants = {}


# @input_error
def find_contacts(value: str) -> str:
    contacts = constants.ADDRESS_BOOK.search_contacts(value)

    if contacts:
        format_contacts = []

        for contact in contacts:
            phones = [str(x.value) for x in contact.phones]
            birthday = contact.birthday.value if contact.birthday else ''
            address = contact.address.value if contact.value else None
            email = contact.email.value if contact.value else None

            contact = f"{contact.name.value} : {birthday} : {', '.join(phones)} : {email} : {address}"
            format_contacts.append(contact)

        return '\n'.join(format_contacts)


if __name__ == '__main__':
    main()

class Address(Field):
        def __init__(self, street: str, city: str, country: str):
            self.street = street
            self.city = city
            self.city = country


#TODO - to add in AddressBook, below

 # Temporary command due to impossibility to change object in the file

def change_contact(self, contact: Record, remove: bool = False) -> None:
    temporary_filename = 'old_contacts.json'

    os.rename(self.file_name, temporary_filename)

    self.file_name = temporary_filename

    for _contact in self.__read_file():
        if _contact.name.value == contact.name.value:
            if remove:
                continue

            AddressBook().add_record(contact)

        else:
            AddressBook().add_record(_contact)

        os.remove(temporary_filename)
        self.file_name = AddressBook().file_name


#TODO  - to do add in AddressBook as its method
 #    adding contacts(email and address) into the AddressBook
 def add_record(self, record: Record):
     contact = {
            'name': record.name.value,
            'phones': [x.value for x in record.phones],
            'birthday': record.birthday.value.strftime('%d.%m.%Y') if record.birthday else None,
            'address': record.address.value if record.value else None,
            'email': record.email.value if record.value else None
     }

#TODO - to add in the "class Record"

    def delete_phone(self, phone: str) -> str | None:
        for phone_ in self.phones:
            if phone_.value == phone:
                self.phones.remove(phone_)
                return phone

    def update_phone(self, old_phone: str, new_phone: str) -> str | None:
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return new_phone

    def change_birthday(self, birthday: str) -> Birthday:
        self.birthday = Birthday(birthday)
        return self.birthday

    def update_email(self, old_email: str, new_email: str) -> str |None:
        for email in self.email:
            if email.value == old_email:
                email.value = new_email
                return new_email

    def delete_email(self, email: str) -> str | None:
        for email_ in self.email:
            if email_.value == email:
                self.email.remove(email_)
                return email
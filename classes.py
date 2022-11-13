from collections import UserDict
from datetime import datetime

class Address(Field):
    pass
    
class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
           if datetime.strptime(value, '%d.%m.%Y'):
              self.__value = value
        except:
            self.__value = None

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.address = None
        self.phones = []
        self.email = None
        self.birthday = None

    def add_address(self, address):
        user_address = Address(address)
        if user_address.value:
            self.address = Address(address)
            return True

    def add_phone(self, phone):
        user_phone = Phone(phone)
        if user_phone.value:
            self.phones.append(Phone(phone))
            return True

    def add_email(self, email):
        user_email = Email(email)
        if user_email.value:
            self.email = Email(email)
            return True

    def add_birthday(self, birthday):
        user_birthday = Birthday(birthday)
        if user_birthday.value:
            self.birthday = Birthday(birthday)
            return True

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record    
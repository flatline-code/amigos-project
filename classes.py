import re
from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"

class Address(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    
class Birthday(Field):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
           if datetime.strptime(value, '%d.%m.%Y'):
              self._value = value
        except (ValueError, TypeError):
            self._value = None

class Name(Field):
   pass


class Phone(Field):

    @Field.value.setter
    def value(self, value):
        self._value = self.check_phone(value)

    @staticmethod
    def check_phone(phone: str) -> str:
        pattern = r"(^380|0|80)\d{9}$"
        match = re.fullmatch(pattern, phone)
        if not match:
            raise ValueError("Invalid, please enter a valid phone number")

        return phone


class Email(Field):

    @Field.value.setter
    def value(self, value: str):
        self._value = self._check_email(value)

    @staticmethod
    def _check_email(_email: str) -> str:
        format = r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}"

        if not re.match(format, _email):
            raise ValueError(f"Invalid email format: {_email}. Email format should be name@domain.com")

        return _email

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.address = None
        self.phones = []
        self.email = None
        self.birthday = None

    def add_address(self, address):
        self.address = Address(address)
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_email(self, email):
        self.email = Email(email)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record    
import re


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

        # print('You entered the correct email')
        return _email

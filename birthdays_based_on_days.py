from datetime import datetime, timedelta, date

# TODO - to add in handlers

@input_error
def get_birthdays(days: str) -> str:

    try:
        days = int(days)
    except ValueError:
        raise ValueError("You have to enter the days as an even number.")

    day_of_bd = date.today() + timedelta(days)
    list_of_birthdays = ''

    for name, record in address_book.items():
        if not record.birthday:
            continue

        birthday = datetime.strptime(record.birthday.value, '%d.%m.%Y')

        if day_of_bd.month == birthday.month and day_of_bd.day == birthday.day:
            birthday = str(record.birthday.value) if record.birthday else '-'
            list_of_birthdays += f'{record.name.value}: {birthday}\n'

    return list_of_birthdays or "There is no people, who has birthdays on this particular day."


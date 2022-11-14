#TODO - to create a folder "handlers" and import input_error


@input_error
def update_phone(name: str, old_phone: str, new_phone: str) -> str:
    contact: Record | None = constants.ADDRESS_BOOK[name]
    updated_phone = contact.update_phone(old_phone, new_phone)

    if updated_phone:
        constants.ADDRESS_BOOK.change_contact(contact)  # have to add additional step because of data is saved in the filefor future added
        # option = JSON).

        return f"The old phone {old_phone} was updated to a new one {new_phone}."

    return f"The number {old_phone} of this person was not located in the list."


@input_error
def delete_phone(name: str, phone: str):
    contact: Record | None = constants.ADDRESS_BOOK[name]

    deleted_phone = contact.delete_phone(phone)

    if deleted_phone:
        constants.ADDRESS_BOOK.change_contact(contact)  # have to add additional step because of data is saved in the file (for future added
        # option = JSON)

        return f"The phone number {phone} for {name} was removed."

    return f"The number {phone} of this person was not located in the list."


@input_error
def update_birthday(name: str, birthday: str) -> str:
    contact: Record | None = constants.ADDRESS_BOOK[name]

    contact.change_birthday(birthday)
    constants.ADDRESS_BOOK.change_contact(contact)  # have to add additional step because of data is saved in the file (for future added
        # option = JSON).
    return f"The birthday of this person, {name}, was change to {contact.birthday.value}"


@input_error
def update_address(address: str, old_address: str, new_address: str) -> str:
    contact: Record | None = constants.ADDRESS_BOOK[address]
    updated_address = contact.update_address(old_address, new_address)

    if updated_address:
        constants.ADDRESS_BOOK.change_contact(contact)  # have to add additional step because of data is saved in the file (for future added
        # option = JSON).
        return f"The old address {old_address} was updated to a new one {new_address}."

    return f"The address {old_address} of this person was not located in the list."


@input_error
def delete_address(address: str, name: str) -> str:
    contact: Record | None = constants.ADDRESS_BOOK[address]

    deleted_address = contact.delete_address(address)

    if deleted_address:
        constants.ADDRESS_BOOK.change_contact(contact)  # have to add additional step because of data is saved in the file (for future added
        # option = JSON).
        return f"The address {address} for {name} was removed."

    return f"The address {address} of this person was not located in the list."
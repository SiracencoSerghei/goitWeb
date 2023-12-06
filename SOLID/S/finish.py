class ValidPhoneException(Exception):
    def __init__(self, message='NOT valid phone'):
        super().__init__(message)


class PersonFormatterInfo:

    def value_of(self):
        raise NotImplementedError


class PersonAddress(PersonFormatterInfo):
    def __init__(self, city: str, street: str, house: int):
        self.city = city
        self.street = street
        self.house = house

    def value_of(self):
        return f"City: {self.city} Street: {self.street} house: {self.house}"


class PersonPhoneNumber(PersonFormatterInfo):
    def __init__(self, phone: str, operator_code: str):
        # validation:
        if operator_code != '050':
            raise ValidPhoneException

        self.phone = phone
        self.operator_code = operator_code

    def value_of(self):
        return f"+38({self.operator_code}){self.phone}"


class Person:
    def __init__(self, name: str, phone: PersonFormatterInfo, address: PersonFormatterInfo):
        self.name = name
        self.phone = phone
        self.address = address

    def get_phone_number(self):
        return f"{self.name}: {self.phone.value_of()}"

    def get_address(self):
        return f"{self.name}: {self.address.value_of()}"


if __name__ == '__main__':
    try:
        phone = PersonPhoneNumber('5463748', '050')
        address = PersonAddress('Denderleeuw', 'Stationweg', 25)
        person = Person('Sergio', phone, address)
        print(person.get_phone_number())
        print(person.get_address())
    except ValidPhoneException as e:
        print(f"Error: {e}")

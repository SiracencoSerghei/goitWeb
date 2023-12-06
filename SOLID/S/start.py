class Person:
    def __init__(self, name, phone,  city, street, house):
        self.name = name
        self.phone = phone
        self.city = city
        self.street = street
        self.house = house

    def get_address(self):
        return f'{self.city}, {self.street}, {self.house}'


person = Person('Alexander', '36007', 'Poltava', 'European', 28)
print(person.get_address())
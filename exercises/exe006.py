class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    def print_person(self):
        return f'Nome: {self.name}; Endereço: {self.address}; Telefone: {self.phone}'

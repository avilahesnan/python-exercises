class Person:

    def __init__(self, name: str, address: str, phone: str) -> None:
        self.__name: str = name
        self.__address: str = address
        self.__phone: str = phone

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, new_address: str) -> None:
        self.__address = new_address

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, new_phone: str) -> None:
        self.__phone = new_phone

    def print_person(self) -> str:
        return f'Nome: {self.name}; Endereço: {self.address}; Telefone: {self.phone}'

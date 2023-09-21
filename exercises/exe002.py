class Person:

    def __init__(self, name: str, age: int, height: int) -> None:
        self.__name: str = name
        self.__age: int = age
        self.__height: int = height

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: int) -> None:
        self.__age = new_age

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, new_height: int) -> None:
        self.__height = new_height

    def print_person(self) -> str:
        return f'{self.name} tem {self.age} anos e altura {self.height}cm'

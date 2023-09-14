class Person:

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_age(self):
        return self.__name

    def set_age(self, value):
        self.__age = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        self.__height = value

    def print_person(self):
        print(f'{self.__name} tem {self.__age} anos e altura {self.__height}cm')


user1 = Person('Hesnan', 23, 175)
user1.print_person()

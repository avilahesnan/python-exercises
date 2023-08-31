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
        return self.__age

    def set_age(self, value):
        self.__age = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        self.__height = value

    def data(self):
        print(f'{self.__name} com {self.__age} anos e {self.__height}cm de altura')


pessoa1 = Person('Hesnan', 23, 175)
pessoa1.data()

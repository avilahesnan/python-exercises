class Person:

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def height(self):
        return self.__height

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    def print_person(self):
        print(f'{self.name} tem {self.age} anos e altura {self.height}cm')


user1 = Person('Hesnan', 23, 175)
user1.print_person()

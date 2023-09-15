class Diary:

    list_store = []

    @classmethod
    def print_diary(cls):
        return Diary.list_store

    @classmethod
    def print_person(cls, index):
        return Diary.list_store[index]

    @classmethod
    def search_person(cls, name):
        for k, person in enumerate(Diary.list_store):
            if name == person[0]:
                return f'{name} está na posição: {k}'

    @classmethod
    def remove_person(cls, name):
        for k, person in enumerate(Diary.list_store):
            if name == person[0]:
                Diary.list_store.pop(k)
                return f'{person[0]} foi excluído com sucesso!'

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

    def store_person(self):
        if len(Diary.list_store) < 10:
            Diary.list_store.append([self.name, self.age, self.height])
            return print(f'{self.name} foi adicionado com sucesso!')

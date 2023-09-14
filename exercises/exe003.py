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

    def store_person(self):
        if len(Diary.list_store) < 10:
            Diary.list_store.append([self.__name, self.__age, self.__height])
            return print(f'{self.__name} foi adicionado com sucesso!')


user1 = Diary('hesnan', 23, 175)
user2 = Diary('elon', 25, 171)
user3 = Diary('werik', 22, 180)
user1.store_person()
user2.store_person()
user3.store_person()

print(Diary.print_diary())
print(user1.print_person(0))
print(user1.search_person('elon'))
print(user1.remove_person('werik'))

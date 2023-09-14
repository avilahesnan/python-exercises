class Schedule:

    list_store = []

    @classmethod
    def print_schedule(cls):
        return Schedule.list_store

    @classmethod
    def print_person(cls, index):
        return Schedule.list_store[index]

    @classmethod
    def search_person(cls, name):
        for k, person in enumerate(Schedule.list_store):
            if name == person[0]:
                return f'{name} está na posição: {k}'

    @classmethod
    def remove_person(cls, name):
        for k, person in enumerate(Schedule.list_store):
            if name == person[0]:
                Schedule.list_store.pop(k)
                return f'{person[0]} foi excluído com sucesso!'

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def store_person(self):
        Schedule.list_store.append([self.__name, self.__age, self.__height])
        return print(f'{self.__name} foi adicionado com sucesso!')


user1 = Schedule('hesnan', 23, 175)
user2 = Schedule('elon', 25, 171)
user3 = Schedule('werik', 22, 180)
user1.store_person()
user2.store_person()
user3.store_person()
print(Schedule.print_schedule())
print(user1.print_person(0))
print(user1.search_person('elon'))
print(user1.remove_person('werik'))

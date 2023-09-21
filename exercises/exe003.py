from typing import List


class Diary:

    list_store: List[list] = []

    @classmethod
    def print_diary(cls) -> list:
        return Diary.list_store

    @classmethod
    def print_person(cls, index: int) -> list:
        return Diary.list_store[index]

    @classmethod
    def search_person(cls, name: str) -> None:
        for k, person in enumerate(Diary.list_store):
            if name == person[0]:
                return print(f'{name} está na posição: {k}')

    @classmethod
    def remove_person(cls, name: str) -> None:
        for k, person in enumerate(Diary.list_store):
            if name == person[0]:
                Diary.list_store.pop(k)
                return print(f'{person[0]} foi excluído com sucesso!')

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

    def store_person(self) -> None:
        if len(Diary.list_store) < 10:
            Diary.list_store.append([self.name, self.age, self.height])
            return print(f'{self.name} foi adicionado com sucesso!')

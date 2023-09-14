class Lift:

    def __init__(self, stories, capacity):
        self.__current_floor = 0
        self.__stories = stories
        self.__capacity = capacity
        self.__quantity_people = 0

    def get_current_floor(self):
        return self.__current_floor

    def set_current_floor(self, value):
        self.__current_floor = value

    def get_stories(self):
        return self.__stories

    def set_stories(self, value):
        self.__stories = value

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, value):
        self.__capacity = value

    def get_quantity_people(self):
        return self.__quantity_people

    def set_quantity_people(self, value):
        self.__quantity_people = value

    def enter_lift(self):
        if self.__quantity_people < self.__capacity:
            self.__quantity_people += 1
            return print('Entrou!')
        return print(f'O elevador tem {self.__capacity} pessoas, está cheio')

    def exit_lift(self):
        if self.__quantity_people > 0:
            self.__quantity_people -= 1
            return print('Saiu!')
        return print('Não tem ninguém no elevador')

    def up_lift(self):
        if self.__current_floor < self.__stories:
            self.__current_floor += 1
            return print('Subindo...')
        return print(f'Estamos no {self.__stories}º andar, o último')

    def down_lift(self):
        if self.__current_floor > 0:
            self.__current_floor -= 1
            return print('Descendo...')
        return print('Estamos no térreo')


lift = Lift(2, 3)

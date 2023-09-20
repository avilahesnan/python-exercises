class Lift:

    def __init__(self, stories, capacity):
        self.__current_floor = 0
        self.__stories = stories
        self.__capacity = capacity
        self.__quantity_people = 0

    @property
    def current_floor(self):
        return self.__current_floor

    @property
    def stories(self):
        return self.__stories

    @property
    def capacity(self):
        return self.__capacity

    @property
    def quantity_people(self):
        return self.__quantity_people

    @current_floor.setter
    def current_floor(self, new_current_floor):
        self.__current_floor = new_current_floor

    @stories.setter
    def stories(self, new_stories):
        self.__stories = new_stories

    @capacity.setter
    def capacity(self, new_capacity):
        self.__capacity = new_capacity

    @quantity_people.setter
    def quantity_people(self, new_quantity_people):
        self.__quantity_people = new_quantity_people

    def enter_lift(self):
        if self.quantity_people < self.capacity:
            self.quantity_people += 1
            return 'Entrou!'
        return f'O elevador tem {self.capacity} pessoas, está cheio'

    def exit_lift(self):
        if self.quantity_people > 0:
            self.quantity_people -= 1
            return 'Saiu!'
        return 'Não tem ninguém no elevador'

    def up_lift(self):
        if self.quantity_people > 0:
            if self.current_floor < self.stories:
                self.current_floor += 1
                return 'Subindo...'
            return f'Estamos no {self.stories}º andar, o último'
        return 'É preciso ter pessoas dentro do elevador para utiliza-lo'

    def down_lift(self):
        if self.quantity_people > 0:
            if self.current_floor > 0:
                self.current_floor -= 1
                return 'Descendo...'
            return 'Estamos no térreo'
        return 'É preciso ter pessoas dentro do elevador para utiliza-lo'

class Lift:

    def __init__(self, stories: int, capacity: int) -> None:
        self.__current_floor: int = 0
        self.__stories: int = stories
        self.__capacity: int = capacity
        self.__quantity_people: int = 0

    @property
    def current_floor(self) -> int:
        return self.__current_floor

    @current_floor.setter
    def current_floor(self, new_current_floor: int) -> None:
        self.__current_floor = new_current_floor

    @property
    def stories(self) -> int:
        return self.__stories

    @stories.setter
    def stories(self, new_stories: int) -> None:
        self.__stories = new_stories

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity: int) -> None:
        self.__capacity = new_capacity

    @property
    def quantity_people(self) -> int:
        return self.__quantity_people

    @quantity_people.setter
    def quantity_people(self, new_quantity_people: int) -> None:
        self.__quantity_people = new_quantity_people

    def enter_lift(self) -> str:
        if self.quantity_people < self.capacity:
            self.quantity_people += 1
            return 'Entrou!'
        return f'O elevador tem {self.capacity} pessoas, está cheio'

    def exit_lift(self) -> str:
        if self.quantity_people > 0:
            self.quantity_people -= 1
            return 'Saiu!'
        return 'Não tem ninguém no elevador'

    def up_lift(self) -> str:
        if self.quantity_people > 0:
            if self.current_floor < self.stories:
                self.current_floor += 1
                return 'Subindo...'
            return f'Estamos no {self.stories}º andar, o último'
        return 'É preciso ter pessoas dentro do elevador para utiliza-lo'

    def down_lift(self) -> str:
        if self.quantity_people > 0:
            if self.current_floor > 0:
                self.current_floor -= 1
                return 'Descendo...'
            return 'Estamos no térreo'
        return 'É preciso ter pessoas dentro do elevador para utiliza-lo'

class Equipment:

    def __init__(self, brand: str, model: str) -> None:
        self.__brand: str = brand
        self.__model: str = model

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, new_brand: str) -> None:
        self.__brand = new_brand

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, new_model: str) -> None:
        self.__model = new_model

    def print_device(self) -> None:
        return print(f'Marca: {self.brand}; Modelo: {self.model}')


class Computer(Equipment):

    def __init__(self, brand: str, model: str, processor: str, system: str) -> None:
        super().__init__(brand, model)
        self.__processor: str = processor
        self.__system: str = system

    @property
    def processor(self) -> str:
        return self.__processor

    @processor.setter
    def processor(self, new_processor: str) -> None:
        self.__processor = new_processor

    @property
    def system(self) -> str:
        return self.__system

    @system.setter
    def system(self, new_system: str) -> None:
        self.__system = new_system

    def print_device(self) -> None:
        return print(f'Marca:{self.brand}; Modelo:{self.model}; Processador:{self.processor}; Sistema:{self.system}')


class TestEquipment:

    equip: Equipment = Equipment('lenovo', 'ideapad s145')
    pc: Computer = Computer('lenovo', 'ideapad s145', 'i3 8gen', 'win64')

    @staticmethod
    def main() -> None:
        TestEquipment.equip.print_device()
        TestEquipment.pc.print_device()

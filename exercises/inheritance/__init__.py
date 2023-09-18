class Equipment:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    def print_device(self):
        return print(f'Marca: {self.brand}; Modelo: {self.model}')


class Computer(Equipment):

    def __init__(self, brand, model, processor, system):
        super().__init__(brand, model)
        self.__processor = processor
        self.__system = system

    @property
    def brand(self):
        return super().brand

    @property
    def model(self):
        return super().model

    @property
    def processor(self):
        return self.__processor

    @property
    def system(self):
        return self.__system

    @brand.setter
    def brand(self, new_brand):
        super().brand = new_brand

    @model.setter
    def model(self, new_model):
        super().model = new_model

    @processor.setter
    def processor(self, new_processor):
        self.__processor = new_processor

    @system.setter
    def system(self, new_system):
        self.__system = new_system

    def print_device(self):
        return print(f'Marca:{self.brand}; Modelo:{self.model}; Processador:{self.processor}; Sistema:{self.system}')


class TestEquipment:

    equip = Equipment('lenovo', 'ideapad s145')
    pc = Computer('lenovo', 'ideapad s145', 'i3 8gen', 'win64')

    @staticmethod
    def main():
        TestEquipment.equip.print_device()
        TestEquipment.pc.print_device()

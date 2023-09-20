class Motorbike:

    def __init__(self, brand, model, color, gear_max):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__gear = 0
        self.__gear_max = gear_max
        self.__on = False

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @property
    def gear(self):
        return self.__gear

    @property
    def gear_max(self):
        return self.__gear_max

    @property
    def on(self):
        return self.__on

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @gear.setter
    def gear(self, new_gear):
        self.__gear = new_gear

    @gear_max.setter
    def gear_max(self, new_gear_max):
        self.__gear_max = new_gear_max

    @on.setter
    def on(self, new_on):
        self.__on = new_on

    def print_motorbike(self):
        return (f'Marca: {self.brand}; Modelo: {self.model}; Cor: {self.color}; Marcha Atual: {self.gear};'
                f' Marcha Máxima: {self.gear_max}; Ligada: {self.on}')

    def gear_up(self):
        if self.on:
            if self.gear < self.gear_max:
                self.gear += 1
                return 'Proxima marcha'
        return 'A moto precisa está ligada para subir de marcha!'

    def gear_down(self):
        if self.on:
            if self.gear > 0:
                self.gear -= 1
                return 'Voltar uma marcha'
        return 'A moto precisa está ligada para descer de marcha!'

    def btn_on(self):
        if not self.on:
            self.on = True
            return 'Ligando...'
        else:
            self.on = False
            return 'Desligando...'

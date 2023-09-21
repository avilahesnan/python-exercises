class Motorbike:

    def __init__(self, brand: str, model: str, color: str, gear_max: int) -> None:
        self.__brand: str = brand
        self.__model: str = model
        self.__color: str = color
        self.__gear: int = 0
        self.__gear_max: int = gear_max
        self.__on: bool = False

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

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, new_color: str) -> None:
        self.__color = new_color

    @property
    def gear(self) -> int:
        return self.__gear

    @gear.setter
    def gear(self, new_gear: int) -> None:
        self.__gear = new_gear

    @property
    def gear_max(self) -> int:
        return self.__gear_max

    @gear_max.setter
    def gear_max(self, new_gear_max: int) -> None:
        self.__gear_max = new_gear_max

    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, new_on: bool) -> None:
        self.__on = new_on

    def print_motorbike(self) -> str:
        return (f'Marca: {self.brand}; Modelo: {self.model}; Cor: {self.color}; Marcha Atual: {self.gear};'
                f' Marcha Máxima: {self.gear_max}; Ligada: {self.on}')

    def gear_up(self) -> str:
        if self.on:
            if self.gear < self.gear_max:
                self.gear += 1
                return 'Proxima marcha'
        return 'A moto precisa está ligada para subir de marcha!'

    def gear_down(self) -> str:
        if self.on:
            if self.gear > 0:
                self.gear -= 1
                return 'Voltar uma marcha'
        return 'A moto precisa está ligada para descer de marcha!'

    def btn_on(self) -> str:
        if not self.on:
            self.on = True
            return 'Ligando...'
        else:
            self.on = False
            return 'Desligando...'

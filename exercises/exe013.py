class Microwave:

    def __init__(self) -> None:
        self.__on: bool = False
        self.__closed: bool = True

    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, new_on: bool) -> None:
        self.__on = new_on

    @property
    def closed(self) -> bool:
        return self.__closed

    @closed.setter
    def closed(self, new_closed: bool) -> None:
        self.__closed = new_closed

    def print_microwave(self) -> str:
        return f'Ligado: {self.on}; Fechado: {self.closed}'

    def btn_on(self) -> str:
        if self.closed:
            if not self.on:
                self.on = True
                return 'Ligado'
            else:
                self.on = False
                return 'Cancelado'
        else:
            return 'A porta precisa está fechada!'

    def btn_door(self) -> str:
        if not self.closed:
            self.closed = True
            return 'A porta está fechada!'
        else:
            self.closed = False
            return 'A porta está aberta!'

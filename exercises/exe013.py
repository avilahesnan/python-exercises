class Microwave:

    def __init__(self):
        self.__on = False
        self.__closed = True

    @property
    def on(self):
        return self.__on

    @property
    def closed(self):
        return self.__closed

    @on.setter
    def on(self, new_on):
        self.__on = new_on

    @closed.setter
    def closed(self, new_closed):
        self.__closed = new_closed

    def print_microwave(self):
        return f'Ligado: {self.on}; Fechado: {self.closed}'

    def btn_on(self):
        if self.closed:
            if not self.on:
                self.on = True
                return 'Ligado'
            else:
                self.on = False
                return 'Cancelado'
        else:
            return 'A porta precisa está fechada!'

    def btn_door(self):
        if not self.closed:
            self.closed = True
            return 'A porta está fechada!'
        else:
            self.closed = False
            return 'A porta está aberta!'

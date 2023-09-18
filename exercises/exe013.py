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
        return print(f'Ligado: {self.on}; Fechado: {self.closed}')

    def btn_on(self):
        if self.closed:
            if not self.on:
                self.on = True
                return print('Ligado')
            else:
                self.on = False
                return print('Cancelado')
        else:
            return print('A porta precisa está fechada!')

    def btn_door(self):
        if not self.closed:
            self.closed = True
            return print('A porta fechou!')
        else:
            self.closed = False
            return print('A porta Abriu!')

class HomeAppliance:

    def __init__(self):
        self.__on = False

    @property
    def on(self):
        return self.__on

    @on.setter
    def on(self, new_on):
        self.__on = new_on

    def btn_on(self):
        if not self.on:
            self.on = True
            return print('Ligando...')
        else:
            self.on = False
            return print('Desligando...')

    def print_home_appliance(self):
        return print(f'Ligado: {self.on}')

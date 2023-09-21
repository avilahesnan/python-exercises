class HomeAppliance:

    def __init__(self) -> None:
        self.__on: bool = False

    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, new_on: bool) -> None:
        self.__on = new_on

    def btn_on(self) -> str:
        if not self.on:
            self.on = True
            return 'Ligando...'
        else:
            self.on = False
            return 'Desligando...'

    def print_home_appliance(self) -> str:
        return f'Ligado: {self.on}'

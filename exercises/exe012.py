class Television:

    def __init__(self, channel: int, volume: int, channel_max: int, volume_max: int) -> None:
        self.__channel: int = channel
        self.__volume: int = volume
        self.__channel_max: int = channel_max
        self.__volume_max: int = volume_max
        self.__on: bool = False

    @property
    def channel(self) -> int:
        return self.__channel

    @channel.setter
    def channel(self, new_channel: int) -> None:
        self.__channel = new_channel

    @property
    def volume(self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, new_volume: int) -> None:
        self.__volume = new_volume

    @property
    def channel_max(self) -> int:
        return self.__channel_max

    @channel_max.setter
    def channel_max(self, new_channel_max: int) -> None:
        self.__channel_max = new_channel_max

    @property
    def volume_max(self) -> int:
        return self.__volume_max

    @volume_max.setter
    def volume_max(self, new_volume_max: int) -> None:
        self.__volume_max = new_volume_max

    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, new_on: bool) -> None:
        self.__on = new_on

    def print_tv(self) -> str:
        return (f'Ligada: {self.on}; Total de Canais: {self.channel_max}; Canal Atual: {self.channel};'
                f' Volume Máximo: {self.volume_max}; Volume Atual: {self.volume}')

    def btn_on(self) -> str:
        if not self.on:
            self.on = True
            return 'Ligando...'
        else:
            self.on = False
            return 'Desligando...'

    def volume_up(self) -> str:
        if self.on:
            if self.volume < self.volume_max:
                self.volume += 1
                return f'Volume: {self.volume}'
            return f'Volume: {self.volume}'
        return 'O televisor está desligado'

    def volume_down(self) -> str:
        if self.on:
            if self.volume > 0:
                self.volume -= 1
                return f'Volume: {self.volume}'
            return f'Volume: {self.volume}'
        return 'O televisor está desligado'

    def channel_next(self) -> str:
        if self.on:
            if self.channel < self.channel_max:
                self.channel += 1
                return f'Canal: {self.channel}'
            else:
                self.channel = 1
                return f'Canal: {self.channel}'
        return 'O televisor está desligado'

    def channel_previous(self) -> str:
        if self.on:
            if self.channel > 1:
                self.channel -= 1
                return f'Canal: {self.channel}'
            else:
                self.channel = self.channel_max
                return f'Canal: {self.channel}'
        return 'O televisor está desligado'

class Television:

    def __init__(self, channel, volume, channel_max, volume_max):
        self.__channel = channel
        self.__volume = volume
        self.__channel_max = channel_max
        self.__volume_max = volume_max
        self.__on = False

    @property
    def channel(self):
        return self.__channel

    @property
    def volume(self):
        return self.__volume

    @property
    def channel_max(self):
        return self.__channel_max

    @property
    def volume_max(self):
        return self.__volume_max

    @property
    def on(self):
        return self.__on

    @channel.setter
    def channel(self, new_channel):
        self.__channel = new_channel

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    @channel_max.setter
    def channel_max(self, new_channel_max):
        self.__channel_max = new_channel_max

    @volume_max.setter
    def volume_max(self, new_volume_max):
        self.__volume_max = new_volume_max

    @on.setter
    def on(self, new_on):
        self.__on = new_on

    def print_tv(self):
        return print(f'Ligada: {self.on}; Total de Canais: {self.channel_max}; Canal Atual: {self.channel};'
                     f' Volume Máximo: {self.volume_max}; Volume Atual: {self.volume}')

    def btn_on(self):
        if not self.on:
            self.on = True
            return print('Ligando...')
        else:
            self.on = False
            return print('Desligando...')

    def volume_up(self):
        if self.on:
            if self.volume < self.volume_max:
                self.volume += 1
                return print(f'Volume: {self.volume}')
            return print(f'Volume: {self.volume}')
        return print('O televisor está desligado')

    def volume_down(self):
        if self.on:
            if self.volume > 0:
                self.volume -= 1
                return print(f'Volume: {self.volume}')
            return print(f'Volume: {self.volume}')
        return print('O televisor está desligado')

    def channel_next(self):
        if self.on:
            if self.channel < self.channel_max:
                self.channel += 1
                return print(f'Canal: {self.channel}')
            else:
                self.channel = 1
                return print(f'Canal: {self.channel}')
        return print('O televisor está desligado')

    def channel_previous(self):
        if self.on:
            if self.channel > 1:
                self.channel -= 1
                return print(f'Canal: {self.channel}')
            else:
                self.channel = self.channel_max
                return print(f'Canal: {self.channel}')
        return print('O televisor está desligado')

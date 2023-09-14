class Television:

    total_channels = 100
    volume = 50
    current_channel = 1
    on = False


class RemoteControl:

    @staticmethod
    def on():
        if not Television.on:
            Television.on = True
        else:
            Television.on = False

    @staticmethod
    def increase_volume():
        if Television.on:
            if Television.volume < 100:
                Television.volume += 1
                return print(Television.volume)
            return print(f'O volume está no máximo {Television.volume}')

    @staticmethod
    def decrease_volume():
        if Television.on:
            if Television.volume > 0:
                Television.volume -= 1
                return print(Television.volume)
            return print(f'O volume está mo mínimo {Television.volume}')

    @staticmethod
    def choice_channel(channel):
        if Television.on:
            Television.current_channel = channel
            return print(Television.current_channel)

    @staticmethod
    def increase_channel():
        if Television.on:
            if Television.total_channels < 100:
                Television.current_channel += 1
                return print(Television.current_channel)
            return print(f'Não tem outros canais depois do canal {Television.current_channel}')

    @staticmethod
    def decrease_channel():
        if Television.on:
            if Television.current_channel > 0:
                Television.current_channel -= 1
                return print(Television.current_channel)
            return print(f'Não tem outros canais antes do canal {Television.current_channel}')

    @staticmethod
    def consult_channel():
        if Television.on:
            return print(f'Canal: {Television.current_channel}')

    @staticmethod
    def consult_volume():
        if Television.on:
            return print(f'Volume: {Television.volume}')

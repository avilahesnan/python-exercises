from typing import Union


class Television:

    total_channels: int = 100
    volume: int = 50
    current_channel: int = 1
    on: bool = False


class RemoteControl:

    @staticmethod
    def on() -> None:
        if not Television.on:
            Television.on = True
        else:
            Television.on = False

    @staticmethod
    def increase_volume() -> Union[int, str, None]:
        if Television.on:
            if Television.volume < 100:
                Television.volume += 1
                return Television.volume
            return f'O volume está no máximo {Television.volume}'
        return None

    @staticmethod
    def decrease_volume() -> Union[int, str, None]:
        if Television.on:
            if Television.volume > 0:
                Television.volume -= 1
                return Television.volume
            return f'O volume está mo mínimo {Television.volume}'
        return None

    @staticmethod
    def choice_channel(channel) -> Union[int, None]:
        if Television.on:
            Television.current_channel = channel
            return Television.current_channel
        return None

    @staticmethod
    def increase_channel() -> Union[int, str, None]:
        if Television.on:
            if Television.total_channels < 100:
                Television.current_channel += 1
                return Television.current_channel
            return f'Não tem outros canais depois do canal {Television.current_channel}'
        return None

    @staticmethod
    def decrease_channel() -> Union[int, str, None]:
        if Television.on:
            if Television.current_channel > 0:
                Television.current_channel -= 1
                return Television.current_channel
            return f'Não tem outros canais antes do canal {Television.current_channel}'
        return None

    @staticmethod
    def consult_channel() -> Union[str, None]:
        if Television.on:
            return f'Canal: {Television.current_channel}'
        return None

    @staticmethod
    def consult_volume() -> Union[str, None]:
        if Television.on:
            return f'Volume: {Television.volume}'
        return None

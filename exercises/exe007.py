class Square:

    def __init__(self, side: float) -> None:
        self.__side: float = side
        self.__area: float = Square.calculate_area(self)
        self.__perimeter: float = Square.calculate_perimeter(self)

    @property
    def side(self) -> float:
        return self.__side

    @side.setter
    def side(self, new_side: float) -> None:
        self.__side = new_side

    @property
    def area(self) -> float:
        return self.__area

    @area.setter
    def area(self, new_area: float) -> None:
        self.__area = new_area

    @property
    def perimeter(self) -> float:
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, new_perimeter: float) -> None:
        self.__perimeter = new_perimeter

    def calculate_area(self) -> float:
        self.__area = self.side * self.side
        return self.__area

    def calculate_perimeter(self) -> float:
        self.__perimeter = self.side * 4
        return self.__perimeter

    def print_square(self) -> str:
        return f'O quadrado de lado {self.side} tem área de {self.area} e perímetro de {self.perimeter}'

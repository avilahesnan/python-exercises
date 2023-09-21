class Rectangle:

    def __init__(self, length: float, width: float) -> None:
        self.__length: float = length
        self.__width: float = width
        self.__area: float = Rectangle.calculate_area(self)
        self.__perimeter: float = Rectangle.calculate_perimeter(self)

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, new_length: float) -> None:
        self.__length = new_length

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, new_width: float) -> None:
        self.__width = new_width

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
        self.__area = self.__length * self.__width
        return self.__area

    def calculate_perimeter(self) -> float:
        self.__perimeter = (self.__length * 2) + (self.__width * 2)
        return self.__perimeter

    def print_rectangle(self) -> str:
        return f'Comprimento: {self.length}; Largura: {self.width}; Área: {self.area}; Perímetro: {self.perimeter}'

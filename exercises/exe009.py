from math import pi


class Circle:

    def __init__(self, radius: float) -> None:
        self.__radius: float = radius
        self.__area: float = Circle.calculate_area(self)
        self.__perimeter: float = Circle.calculate_perimeter(self)

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, new_radius: float) -> None:
        self.__radius = new_radius

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
        self.__area = pi * self.radius**2
        return self.__area

    def calculate_perimeter(self) -> float:
        self.__perimeter = 2 * pi * self.radius
        return self.__perimeter

    def print_circle(self) -> str:
        return f'Raio: {self.radius}; Área: {self.area}; Perímetro: {self.perimeter}'

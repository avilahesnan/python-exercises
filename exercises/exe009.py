from math import pi


class Circle:

    def __init__(self, radius):
        self.__radius = radius
        self.__area = Circle.calculate_area(self)
        self.__perimeter = Circle.calculate_perimeter(self)

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius

    @area.setter
    def area(self, new_area):
        self.__area = new_area

    @perimeter.setter
    def perimeter(self, new_perimeter):
        self.__perimeter = new_perimeter

    def calculate_area(self):
        self.__area = pi * self.radius**2
        return self.__area

    def calculate_perimeter(self):
        self.__perimeter = 2 * pi * self.radius
        return self.__perimeter

    def print_circle(self):
        return f'Raio: {self.radius}; Área: {self.area}; Perímetro: {self.perimeter}'

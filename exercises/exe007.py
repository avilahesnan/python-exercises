class Square:

    def __init__(self, side):
        self.__side = side
        self.__area = Square.calculate_area(self)
        self.__perimeter = Square.calculate_perimeter(self)

    @property
    def side(self):
        return self.__side

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    @side.setter
    def side(self, new_side):
        self.__side = new_side

    @area.setter
    def area(self, new_area):
        self.__area = new_area

    @perimeter.setter
    def perimeter(self, new_perimeter):
        self.__perimeter = new_perimeter

    def calculate_area(self):
        self.__area = self.side * self.side
        return self.__area

    def calculate_perimeter(self):
        self.__perimeter = self.side * 4
        return self.__perimeter

    def print_square(self):
        return print(f'O quadrado de lado {self.side} tem área de {self.area} e perímetro de {self.perimeter}')

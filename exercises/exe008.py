class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__area = Rectangle.calculate_area(self)
        self.__perimeter = Rectangle.calculate_perimeter(self)

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def area(self):
        return self.__area

    @property
    def perimeter(self):
        return self.__perimeter

    @length.setter
    def length(self, new_length):
        self.__length = new_length

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @area.setter
    def area(self, new_area):
        self.__area = new_area

    @perimeter.setter
    def perimeter(self, new_perimeter):
        self.__perimeter = new_perimeter

    def calculate_area(self):
        self.__area = self.__length * self.__width
        return self.__area

    def calculate_perimeter(self):
        self.__perimeter = (self.__length * 2) + (self.__width * 2)
        return self.__perimeter

    def print_rectangle(self):
        print(f'Comprimento: {self.length}; Largura: {self.width}; Área: {self.area}; Perímetro: {self.perimeter}')

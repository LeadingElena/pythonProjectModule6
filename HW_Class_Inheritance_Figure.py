import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)          # список цветов в формате RGB
        self.__sides = [sides[0]] * self.sides_count          # список сторон (целые числа)
        self.filled = False           # закрашенный, bool

    def get_color(self):     # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b):   # проверяет корректность переданных значений перед установкой нового цвета
        if all(256 > value >= 0 and isinstance(value, int) for value in (r, g, b) ):
            return True

    def set_color(self, r, g, b): # изменяет список цветов после проверки
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):   # проверяет все ли стороны - целые положительные числа и кол-во
                                         # новых сторон совпадает с текущим
        if self.sides_count == len(new_sides) and all(isinstance(side, int) and side > 0 for side in new_sides):
            return True

    def get_sides(self):    #  возвращает значение атрибута __sides
        return self.__sides

    def __len__(self):          # возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):     # изменяет __sides после проверки
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / 2 * 3,1428

    def get_square(self):       # возвращает площадь
        return 3.1428 * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):       # возвращает площадь
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = self.sides_count * sides[0]
        else:
            self.__sides = [1] * self.sides_count

    def set_sides(self, *new_sides):
        if self._Figure__is_valid_sides(*new_sides):
            if len(new_sides) == 1:
                self.__sides = self.sides_count * new_sides[0]
            else:
                self.__sides = [1] * self.sides_count

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


#Выходные данные (консоль):

#[55, 66, 77]
#[222, 35, 130]
#[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
#[15]
#15
#216
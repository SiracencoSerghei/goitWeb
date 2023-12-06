from math import pi


class ValidShapeException(Exception):
    def __init__(self, message='NOT valid shape'):
        super().__init__(message)


class Shape:

    def area_of(self):
        raise NotImplementedError


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area_of(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi


class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    def total_area(self) -> float:
        summ = 0
        for el in self.shapes:
            summ += el.area_of()
        return summ


if __name__ == '__main__':
    shapes_list = AreaCalculator([Rect(10, 10),
                                  Circle(20),
                                  Rect(4, 5),
                                  Rect(3, 3),
                                  Square(10)])
    total_area = shapes_list.total_area()
    print(total_area)

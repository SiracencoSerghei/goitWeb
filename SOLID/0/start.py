class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def total_area(shapes):
    sum = 0
    for el in shapes:
        sum += el.width * el.height
    return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Rect(4, 5), Rect(3, 3)]
    area = total_area(shapes)
    print(area)
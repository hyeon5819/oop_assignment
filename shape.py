class Shape():
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = self.radius**2*3.14
        return print(area)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length*self.width
        return print(area)


mycircle = Circle(2)
mycircle.get_area()

myrectangle = Rectangle(2, 4)
myrectangle.get_area()

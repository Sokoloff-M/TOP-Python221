from math import pi

class Circle:
    def __init__(self, radius: float):
        self.radius = radius


    @property
    def length(self):
        return 2 * pi * self.radius
    @property
    def area(self):
        return pi * self.radius**2

    @property
    def length(self):
        return 2 * pi * self.radius

circle = Circle(5)
print(f'{circle.lenght = :.2f}\t{circle.area = :.2f}')
circle.radius = 7
print(f'{circle.lenght = :.2f}\t{circle.area = :.2f}')

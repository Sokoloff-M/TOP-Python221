from math import pi, sqrt


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def length(self):
        return 2 * pi * self.radius

    @property
    def area(self) -> float:
        return pi * self.radius ** 2

    @length.setter
    def length(self, new_lenght: float) -> None:
        self.radius = new_lenght / (2 * pi)

    @area.setter
    def area(self, new_area: float) -> None:
        self.radius = sqrt(new_area / pi)


c1 = Circle(5)
print(f"{c1.radius = }\n{c1.length = }\n{c1.area = }\n")

c1.length = 15.7
print(f"{c1.radius = }\n{c1.length = }\n{c1.area = }\n")

c1.area = 100
print(f"{c1.radius = :.1f}\n{c1.length = :.1f}\n{c1.area = :.1f}\n")

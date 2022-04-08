import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.surface_area_equ = 4 * math.pi * (self.radius ** 2)
        self.volume_equ = 4/3 * math.pi * (self.radius ** 3)

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return self.surface_area_equ

    def volume(self):
        return self.volume_equ

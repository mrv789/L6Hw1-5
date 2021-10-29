class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width, weight, depth):
        self._length = length
        self._width = width
        self.weight = weight
        self.depth = depth

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.depth / 1000
        print(f'Для покрытия всего дорожного полотна понадобится {round(asphalt_mass)} тонн асфальта')


r = Road(20, 5000, 25, 5)
print(r.asphalt_mass())
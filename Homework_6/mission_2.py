class Road:

    def __init__(self, width, length):
        self._length = length
        self._width = width

    def weigh_road(self):
        weigh = self._length * self._width * 25 * 5 / 1000
        print(f"При длинне дорожного покрытия в {self._width} м, ширине в {self._length} м, массе асвальта на\n"
                     f"один мертор квадратный в 25 кг и толщеной асфальта в 5 см, масса асфальта состовит {weigh} т")


road = Road(20, 5000)
road.weigh_road()

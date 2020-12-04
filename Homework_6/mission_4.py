class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f"Машина {self.name} начала движение!")

    def stop(self):
        print(f"Машина {self.name} прекратила движение!")

    def turn(self, direction):
        if  direction == 0:
            print(f"Машина {self.name} повернула налево!")
        else:
            print(f"Машина {self.name} повернула направо!")

    def show_speed(self):
        print(f"{self.name} едет со скорастью {self.speed}км\ч.")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} превышает скорость!")
        else:
            print(f"{self.name} едет со скорастью {self.speed}км\ч.")


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} превышает скорость!")
        else:
            print(f"{self.name} едет со скорастью {self.speed}км\ч.")


class PoliceCar(Car):

    def cop(self):
        print(f"Это полицейская машина - {self.is_police}")

    def color_car(self):
        print(f"Машина {self.color} цвета.")

work_car = WorkCar(70, "Black", "Tesla", 0)
work_car.go()
work_car.turn(0)
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(100, "Black & White", "BMW", 1)
police_car.go()
police_car.cop()
police_car.color_car()
police_car.turn(1)
police_car.show_speed()
police_car.stop()

sport_car = SportCar(210, "Yellow", "Lamborghini", 0)
sport_car.go()
sport_car.turn(0)
sport_car.show_speed()
sport_car.stop()

town_car = TownCar(50, "Grey", "Porsche", 0)
town_car.go()
town_car.turn(1)
town_car.show_speed()
town_car.stop()

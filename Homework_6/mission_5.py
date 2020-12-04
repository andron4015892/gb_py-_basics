class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print(f"Начинаю писать с помощью: {self.title}.")


class Pencil(Stationery):

    def draw(self):
        print(f"Делаю набросок с помощью: {self.title}.")


class Handle(Stationery):

    def draw(self):
        print(f"Расписываюсь на постере с помощью: {self.title}.")


pen = Pen("Ручка")
pen.draw()

pencil = Pencil("Карандаш")
pencil.draw()

handle = Handle("Маркер")
handle.draw()

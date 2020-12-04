class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя работника: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Его оклат с учётом бонусов составляет: {sum(self._income.values())}$")


check = Position("Jozef", "Engelman", "Boss", 3000, 700)
check.get_full_name()
check.get_total_income()

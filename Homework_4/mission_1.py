from sys import argv

script_name, work_hour, cash_hour, bonus = argv


def work_cash():
    """Функция для расчёта ЗП"""
    a = int(work_hour)
    b = int(cash_hour)
    c = int(bonus)
    return a * b + c


print(work_cash())

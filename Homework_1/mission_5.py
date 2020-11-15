proceeds = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
cash = proceeds - cost
if cash > 0:
    print("Фирма приносит прибыль!")
    profitability = cash / proceeds
    print(f"Рентабельность фирмы состовляет: {profitability:.2f}%")
    employees = int(input("Введите колличество сотрудников: "))
    proceeds_employees = cash / employees
    print(f"На каждого сотрудника приходиться {proceeds_employees:.1f} едениц прибыли")
elif cash < 0 :
    print("Фирма убытачна!")
else:
    print("Фирма работает в ноль!")

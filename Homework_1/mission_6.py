a = int(input("Введите свой результат в килломертах: "))
b = int(input("Введите желаемый результат: "))
namber_day = 1
if a >= b:
    print("Ввод не корректен")
    a = int(input("Введите свой результат в килломертах: "))
    b = int(input("Введите желаемый результат: "))
while True:
    if a < b:
        print(f"{namber_day} день: {a:.2f} км.")
        ten_percent = a / 10
        a += ten_percent
        namber_day += 1
    else:
        print(f"На {namber_day} день спортсмен достиг: {a:.2f} км!")
        break

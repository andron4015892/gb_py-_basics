def summa_numbers():
    x = 0
    while True:
        my_numbers = input("Введите числа через пробел,"
                           " q для выхода: ").split()
        for i in my_numbers:
            if i == "q":
                return x
            else:
                x += int(i)
        print(f"Сумма введённых чисел равна: {x}")


print(summa_numbers())
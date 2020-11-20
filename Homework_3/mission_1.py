def division(arg_1, arg_2):
    x = arg_1 / arg_2
    return round(x, 4)

one = int(input("Введите делимое: "))
two = int(input("Введите делитель: "))

while two == 0:
    print("На ноль делить нельзя!")
    two = int(input("Введите делитель: "))


print(f"Вот что получилось: {division(one, two)}")

def my_func_1(x, y):
    x = float(x)
    y = abs(int(y))
    return 1/ x ** y


def my_func_2(x, y):
    x = float(x)
    y = int(y)
    if x <= 0 or y >= 0:
        return "Условие выполнено не верно"
    else:
        alfa = 1
        for i in range(abs(y)):
            alfa *= x
        end = 1 / alfa
        return end


one = input("Введите действительно положительный x, x = ")
two = input("Введите целоый отрицательный y, y = ")


print(my_func_1(one, two))
print(my_func_2(one, two))

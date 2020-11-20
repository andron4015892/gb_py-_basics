def my_func(arg_1, arg_2, arg_3):
    '''Функция вычисляет сумму 2-х больших аргументов'''
    test = [arg_1, arg_2, arg_3]
    a = max(test)
    test.remove(a)
    b = max(test)
    return a + b


one = float(input("Введите первый аргумент :"))
two = float(input("Введите второй аргумент :"))
three = float(input("Введите третий аргумент :"))


print(my_func(one, two, three))

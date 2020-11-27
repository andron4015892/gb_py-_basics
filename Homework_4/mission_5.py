from functools import reduce


def func_multiply(one, two):
    """Перемнодает два числа"""
    return one * two


my_list = [el for el in range(100, 1001) if el % 2 == 0]

final_number = reduce(func_multiply, my_list)

print(final_number)

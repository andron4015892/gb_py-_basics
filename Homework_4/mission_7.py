def fact(number):
    final_num = 1
    for item in range(1, number + 1):
        final_num *= item
        yield f'{item}! = {final_num}'


for el in fact(9):
    print(el)

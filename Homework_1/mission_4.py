number = int(input('Введите целое число : '))
testing_number = 0
while number > 0:
    c = number % 10
    if c >= testing_number:
        testing_number = c
    number = number // 10
print(testing_number)


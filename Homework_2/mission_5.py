start_list = [3, 1]

while True:
    test = input("Хотите добавить число в рэйтинг? Y/N :")
    if test.lower() == "y":
        print(f"Имеющийся рэйтинг: {start_list}")
        number = int(input("Введите натуральное число: "))
        wedge = 0
        for num in start_list:
            if number <= num:
                wedge += 1
        start_list.insert(wedge, number)
    print(start_list)
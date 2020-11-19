test_list = ["name", 25, (1, 2, 3), {4, 3, "dog"}, 3.14, True, [1, 2]]
print(test_list)
max_number = len(test_list)
number = 0
while number < max_number:
    print(type(test_list[number]))
    number += 1
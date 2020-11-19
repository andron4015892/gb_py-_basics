list_add = list(input("Введите числа без пробелов и запятых: "))
print(list_add)

for x in range(1,len(list_add),2):
    list_add[x - 1], list_add[x] = list_add[x], list_add[x - 1]

print(list_add)
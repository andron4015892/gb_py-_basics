string = input("Введите строку разделённую пробелами: ").split()
print(string)
for n, s in enumerate(string, 1):
    if len(s) <= 10:
        print(f"{n} - {s}")
    else:
        print(f"{n} - {s[:10]}")
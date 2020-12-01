from random import randint

with open("mission_5.txt", "w+", encoding="utf-8") as new_file:
    new_list = [randint(1, 100) for i in range(5)]
    new_file.write(" ".join(map(str, new_list)))
    new_file.seek(0)
    print(sum(map(int, new_file.readline().split())))

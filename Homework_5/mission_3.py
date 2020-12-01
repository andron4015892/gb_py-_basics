empty = {}
with open("mission_3.txt", "r", encoding="utf-8") as list_file:
    for section in list_file:
        empty[section.split()[0]] = int(section.split()[1])
    print("Зарплата меньше 20000 у: ")
    for name, money in empty.items():
        if money < 20000:
            print(name)
    average_earnings = sum(empty.values()) / len(empty)
    print(f"Средний заработок: {average_earnings}")

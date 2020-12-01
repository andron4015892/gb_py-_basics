empty_dict = {}

with open("mission_6.txt", "r", encoding="utf-8") as lessons:
    test_lessons = lessons.readlines()
    for obj_1 in test_lessons:
        string_1 = "".join((obj_2 if obj_2 in "1234567890" else " ") for obj_2 in obj_1)
        string_2 = [int(obj) for obj in string_1.split()]
        print(f"{obj_1.split()[0]} {sum(string_2)}")

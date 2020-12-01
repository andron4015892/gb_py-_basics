dict_translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("mission_4_add.txt", "w", encoding="utf-8") as add_file:
    with open("mission_4.txt", "r", encoding="utf-8") as old_file:
        add_file.writelines([section.replace(section.split()[0], dict_translate.get(section.split()[0]))
                             for section in old_file])

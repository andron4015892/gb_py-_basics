with open("creation_file.txt", "w", encoding="utf-8") as creation_file:
    while True:
        text = input("Введите текст, для завершения оставте строку пустой: ")
        if text == "":
            break
        else:
            creation_file.write(f"{text}\n")

def int_func():
    string = input("Введите слова через пробел. Принимаются только маленькие латинские буквы: ").split()
    for word in string:
        long_word = 0
        for long in word:
            if 97 <= ord(long) <= 122:
                long_word += 1
        print(word.title() if long_word == len(word) else f"{word} - только маленькие латинские буквы!")


int_func()
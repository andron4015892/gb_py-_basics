with open("mission_2.txt", "r", encoding="utf-8") as verifiable_file:
    test_list = verifiable_file.readlines()
    for number_srt, number in enumerate(test_list, 1):
        number_words = len(number.split())
        print(f"В строке {number_srt} находится {number_words} слов.")
    print(f"Всего строк: {len(test_list)}")

seconds = int(input("Введите время в секундах:"))
if seconds <= 60:
    print(f"Time: 00:00:{seconds}")
elif seconds >= 60:
    minets = seconds // 60
    seconds_time = seconds % 60
if minets <= 60:
    print(f"Time: 00:{minets}:{seconds_time}")
elif minets >= 60:
    hours = minets // 60
    minets_time = minets % 60
    seconds_time = seconds % 60
    print(f"Time: {hours}:{minets_time}:{hours}")
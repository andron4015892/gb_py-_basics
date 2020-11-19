month = int(input("Введите месяц целым числом от 1 до 12: "))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
year = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима", }

while True :
    if month < 1:
        month = int(input("От 1 до 12: "))
    elif month > 12:
        month = int(input("От 1 до 12: "))
    else:
        break


if month in winter:
    print("Зима")
elif month in spring:
    print("Весна")
elif month in summer:
    print("Лето")
else:
    print("Осень")


if month in year:
    print(year[month])
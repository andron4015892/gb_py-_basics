def my_data():
    name = input("Введите ваше имя - ")
    last_name = input("Введите вашу фамилию - ")
    age = int(input("Введите ваш возраст - "))
    city = input("Введите ваш город - ")
    email = input("Введите ваш email - ")
    phone_number = int(input("Введите ваш номер телефона - "))
    print(f"Вас зовут {name} {last_name}, ваш возраст {age}, "
          f"вы живёте в {city}, ваш эл. почта - {email} и"
          f" ваш номер телефона - {phone_number}")


my_data()
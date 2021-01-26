print("Задача 2: Написание функции, принимающей данные пользователя")

def user_data(name, surname, date_birth, city, email, call_num):
    print(f"Имя: {name}; Фамилия: {surname}; Год рождения: {date_birth}; Город проживания: {city}; Email: {email}; Номер телефона: {call_num}")

user_data(name = input("Имя: "), surname = input("Фамилия: "), date_birth = int(input("Год рождения: ")), city = input("Город проживания: "),
          email =input ("Email: "), call_num =input ("Номер телефона: "))



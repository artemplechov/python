print("Задание: Ввод номера месяца и определение времени года. Реализация через list")

number = int(input("Введите номер месяца: "))
year_time = ['зима','зима','весна','весна','весна',',лето',',лето',',лето','осень','осень','осень','зима']
print(f"Время года: {year_time[number-1]}")

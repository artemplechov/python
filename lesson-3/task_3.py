print("Задача 3: Написание функции, которая выводит сумму двух наибольших аргументов")

def my_func(a,b,c):
    if (a >= b) & (b >= c):
        sum = a + b
    elif (b >= a) & (c >= a):
        sum = b + c
    elif (a >= c) & (c >= b):
        sum = a + c
    return sum

a = int(input("Введите аргумент a: "))
b = int(input("Введите аргумент b: "))
c = int(input("Введите аргумент c: "))


print(f"Сумма двух наибольших аргументов = {my_func(a,b,c)}")


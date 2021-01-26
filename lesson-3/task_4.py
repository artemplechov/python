print("Задача 4: Возведение числа в минусовую степень")


def my_func(x,y):
    result = 1
    if (y < 0):
        y = y * (-1)
        result = 1 / x ** y
    elif (y > 0):
        for i in range(y):
            result = result * x
    elif (y == 0):
       result = 1
    return result


x = float(input("Введите число: "))
y = int(input("Введите степень: "))


print(f"x в степени y = {my_func(x,y)}")



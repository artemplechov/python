print("Задание 3. Реализовать программу работы с органическими клетками.")

import time

class OrganicCell():
    def __init__(self, v: int):
        if not isinstance(v, int) or v <= 0:
            raise ValueError("Ошибка! Количество ячеек в клетке может быть только целым числом больше 0")
        self.__v = v

    def __add__(self, other):
        self.sum = self.__v + other.__v
        return self.sum


    def __sub__(self, other):
        self.dif = self.__v - other.__v
        if self.dif <= 0:
            return f"Ошибка! Данная операция приведет к уничтожению клетки"
        else:
            return self.dif


    def __mul__(self, other):
        self.com = self.__v * self.__v
        if self.com == 0:
            return f"Ошибка! Данная операция приведет к уничтожению клетки"
        else:
            return self.com


    def __truediv__(self, other):
        if other.__v <= 0:
            return f"Ошибка! Данная операция невозможна"
        else:
            self.div = self.__v//other.__v
        return self.div



    def __str__(self):
        char_str = "*"
        char_str = char_str * self.__v
        return f'Размер клетки {char_str} яч.'


    def MakeOrder(self, length):
        whole = self.__v // length
        remainder = self.__v % length
        char_str = ""
        j = 1
        for i in range(self.__v):
            if j != length:
                char_str = char_str+"*"
                j += 1
            else:
                char_str = char_str +"*\n"
                j = 1
        return f'{char_str}'





a = OrganicCell(19)
print(a)
b = OrganicCell(3)
print(b)
z = a+b
print(f"Результат сложения клеток = {z} яч.")
z = a-b
print(f"Результат вычитаиня клеток = {z} яч.")
z = a*b
print(f"Результат умножения клеток = {z} яч.")
z = a/b
print(f"Результат деления клеток = {z} яч.")

print(a.MakeOrder(2))
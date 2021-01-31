print("Задача 5. Генерация списка из четных цифр от 100 до 1000 и перемножение всех элементов.")
import random
import functools

my_list = [i for i in range(100,1001) if i % 2 == 0]
print(f"Исходный список из четных элементов от 100 до 1000\n{my_list}")

def my_func(prev_el, el):
    return prev_el*el

print(functools.reduce(my_func, my_list))
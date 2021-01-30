print("Задача 7. Создание генератора с помощью функции с yield.\nФункция высчитывает факториал")
import itertools
import random
n = random.randint(1,6)
print(f"Высчитываем факториал от {n}")

def my_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact =fact*i
        yield fact

j = 1

for i in my_fact(n):
    print(f"{j}! = {i}")
    j += 1





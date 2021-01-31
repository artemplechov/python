import random

print("Задача 3. Из чисел в пределах от 20 до 240 найти числа, кратные 20 или 21")

my_list = [i for i in range(20,241)]

print(f"Исходный список: {my_list}")

kratnoe = random.randint(20,21)
print(f"Будем выводить элементы, кратные {kratnoe}")


my_list = [i for i in range(20,241) if i % kratnoe == 0]

print(f"Итоговый список: {my_list}")
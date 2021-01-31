import random

print("Задача 2. Из списка вывести только те элементы, значения которых больше значения предыдущего элемента")

my_list = []
for i in range(random.randint(0,50)):
    my_list.append(random.randint(0,500))

print(f"Исходный список: {my_list}")

result_list = []

for i in range(len(my_list)-1):
    if my_list[i+1] > my_list[i]:
        result_list.append(my_list[i+1])

print(f"Итоговый список: {result_list}")
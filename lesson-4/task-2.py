import random

print("Задача 2. Из списка вывести только те элементы, значения которых больше значения предыдущего элемента")

#my_list = [i for i in range(random.randint(0,100),random.randint(0,100))]
my_list = []
for i in range(random.randint(0,50)):
    my_list.append(random.randint(0,500))

#my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 100]
print(f"Исходный список: {my_list}")
result_list = []

for i in range(len(my_list)-1):
    if my_list[i+1] > my_list[i]:
        result_list.append(my_list[i+1])



print(f"Итоговый список: {result_list}")
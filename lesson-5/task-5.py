print("Задача 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных\n"
      "пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.")

import random
from functools import reduce

my_list = []
for i in range(random.randint(1,random.randint(15,45))):
    my_list.append(random.randint(1,500))

print(f"Исходный список: {my_list}")

with open("task-5.txt", "w", encoding = "utf-8") as f_obj:
      for i in range(len(my_list)):
            f_obj.write(f"{my_list[i]} ")

my_str = ""
with open("task-5.txt", "r", encoding = "utf-8") as f_obj:
    my_str = f_obj.readline()
print(f"Получены данные из файла: {my_str}")

result = list(map(int,my_str.split()))

sum = reduce(lambda acc, x: acc+x, result)
print(f"Сумма всех чисел из файла = {sum}")

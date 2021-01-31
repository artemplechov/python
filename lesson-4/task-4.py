print("Задача 4. Генерация списка, его обратботка и вывод списка из неповторяющихся элементов")

import random

total_list = []

for i in range(random.randint(0,50)):
    total_list.append(random.randint(0,50))

result_list = []

print(f"Исходный список:\n{total_list}")

total_list.sort()

print(f"Отсортированный исходный список:\n{total_list}\nСортирую только для удобства визуальной проверки")

count = 0

for i in range(len(total_list)):
    count = total_list.count(total_list[i])
    if count == 1:
        result_list.append(total_list[i])

print(f"Итоговый список:\n{result_list}")

# Ниже первый способ решения. Поочередено беру каждый элемент списка и проверяю,
# есть ли он в срезе списка без него самого. Параллено создается пустой список,
# куда записываются 0, если элемента в срезе нет, 1 - если есть.
# Затем прогоняю цикл по всписку и удаляю те элементы, у которых на этой же
# позиции во втором списке стоит 1.
#for i in range(len(total_list)):
 #   a = total_list[i]
  #  print(f"a  {a}")
   # if i < (len(total_list)):
    #    tmp_list = total_list[:i]+total_list[i+1:]
     #   print(f"tmp_list {tmp_list}")
      #  for j in range(len(tmp_list)):
       #     if a == tmp_list[j]:
        #        result_list[i] = 1
    #if i == (len(total_list)):
     #   print(f"a  {a}")
      #  tmp_list = total_list[:i]
       # print(f"tmp_list {tmp_list}")
        #for j in range(len(tmp_list)):
         #   if a == tmp_list[j]:
          #      result_list[i] = 1
#print(f"len of  {len(result_list)}")
#print(f"result_list {result_list}")
#print(f"total_list {total_list}")

#result_list2 = []
#for i in range(len(total_list)):
 #   if result_list[i] == 0:
  #      result_list2.append(total_list[i])
#print(f"Итого {result_list2}")


print("Задание: Ввод списка и обмен элементов с идексами 0 и 1, 2 и 3 и тд.")

my_list = list()
result_list = list()
i = 0
j = 0

list_length = int(input("Введите количество элементов в списке: "))

for i in range(list_length):
   my_list.append(input(f"Введите {i+1} элемент списка: "))
print(f"У нас получился вот такой список:\n {my_list}")

for i in range(int(list_length / 2)):
    result_list.append(my_list[j + 1])
    result_list.append(my_list[j])
    j += 2

if (list_length % 2) != 0:
    result_list.append(my_list[list_length-1])
print(f"Итоговый список: {result_list}")
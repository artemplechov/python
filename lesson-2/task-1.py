print("Задание: Создание списка из элементов разных типов и вывод типа каждого элемента")
my_list = [1,5,44.646,{5, 6, '53BF'},'gfhg',[1,2,'g']]
length = len(my_list)
print(f"Мой список: {my_list}")
print(f"В списке {length} элементов")
i = 0
for i in range(length):
    print(f"{i+1} элемент списка имеет тип {type(my_list[i])}")

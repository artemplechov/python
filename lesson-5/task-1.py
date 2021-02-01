print("Задача 1. Создать программно файл и записать в него построчно данные, вводимые пользователем.")

my_str = ""

with open("task-1.txt", "w") as f_obj:
    print("Введите данные: ")
    while my_str != " "+"\n":
        my_str = input()+"\n"
        f_obj.write(my_str)
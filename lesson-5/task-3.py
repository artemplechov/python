print("Задача 3. Создать не программно файл, записать в него построчно фамилии сотрудников и величину\n"
      "их окладов. Вывести фамилии сотрудников, получающих меньше 20000. Рассчитать среднюю зп.\n")
import json
my_dict = {}
#with open("task-3.txt","r", encoding="utf-8") as f_obj:
f_obj = open("task-3.txt", "r", encoding="utf-8")
#print(f_obj.read())
f_obj.seek(0)
for i in f_obj:

    my_dict[f_obj.readline()] = f_obj.readline()
        #my_dict[i] = list(f_obj.readline())
    print(my_dict)


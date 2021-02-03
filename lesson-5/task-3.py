print("Задача 3. Создать не программно файл, записать в него построчно фамилии сотрудников и величину\n"
      "их окладов. Вывести фамилии сотрудников, получающих меньше 20000. Рассчитать среднюю зп.\n")

my_dict = {}
with open("task-3.txt","r", encoding="utf-8") as f_obj:
    print(f_obj.read())
    f_obj.seek(0)
    for i in f_obj:
        my_dict[i.replace("\n","")] = int(f_obj.readline().replace("\n",""))

average_salary = 0
count = 0
rich_staff = []
for name, salary in my_dict.items():
    average_salary = average_salary+salary
    if salary < 20000:
        count += 1
    else:
        rich_staff.append(name)


print(f"Средняя заработная плата составляет {average_salary/len(my_dict):.2f} руб.")
if count == 0:
    print("Сотрудников, получающих больше 20000руб. нет")
else:
    print(f"Сотрудники, получающие больше 20000руб.: {', '.join(rich_staff)}")



print("Задача 2. Создать не программно файл, сохранить в нем несколько строк, считать эти строки,\n"
      "вывести количество строк и количество символов в каждой строке.")




with open("task-2.txt", "r", encoding = "utf-8") as f_obj:

    my_str = f_obj.read()
    print(my_str)
    f_obj.seek(0)
    for my_str in f_obj:
        my_str = f_obj.readlines()
        print(my_str)
    print(len(my_str))
    for i in range(len(my_str)):
        print(len(my_str[i]))
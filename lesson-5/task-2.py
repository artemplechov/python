print("Задача 2. Создать не программно файл, сохранить в нем несколько строк, считать эти строки,\n"
      "вывести количество строк и количество символов в каждой строке.\n")

with open("task-2.txt", "r", encoding = "utf-8") as f_obj:

    my_str = f_obj.read()
    print(my_str)
    f_obj.seek(0)
    for my_str in f_obj:
        f_obj.seek(0)
        my_str = f_obj.readlines()
    print(f"Количество строк в файле: {len(my_str)}")
    for i in range(len(my_str)):
        tmp_str = my_str[i].split()
        print(f"Количество слов в {i+1} строке: {len(tmp_str)}")
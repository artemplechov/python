print("Задача 4. Создать не программно файл, записать в него построчно пары 'числить - значение'.\n"
      "Числитель записан на английском. Считать строки и заменить английские числители на русские.\n")

en_rus = {"One":"Один - 1", "Two":"Два - 2","Three":"Три - 3 ","Four":"Четыре - 4"}

with open("task-4.txt", "r", encoding = "utf-8") as f_obf:
    for line in f_obf:
        print(line)
        for eng, rus in en_rus.items():
            if line.count(eng.replace("'","")) > 0:
                f_obf_output = open("task-4_output.txt", "a", encoding = "utf-8")
                f_obf_output.write(f"{rus}\n")
                f_obf_output.close
print("Считывание данных выполнено. Проверьте содерживое файл task-4_output.txt")
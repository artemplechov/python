print("Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие\n"
      "лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для\n"
      "каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета\n"
      "и общее количество занятий по нему. Вывести словарь на экран.")

tmp_list = []
count = 0
result_dict = {}
result_list = []
with open("task-6.txt","r", encoding="utf-8") as f_obj:
    for i in f_obj:
        print(i)
        tmp_list = list(i.split())
        tmp_list = [j.replace("(л)","") for j in tmp_list]
        tmp_list = [j.replace("(пр)", "") for j in tmp_list]
        tmp_list = [j.replace("(лаб).", "") for j in tmp_list]
        tmp_list = [j.replace("(лаб)", "") for j in tmp_list]
        count = tmp_list.count("-")
        for k in range(count):
            tmp_list = tmp_list[:tmp_list.index("-")]+tmp_list[tmp_list.index("-")+1:]
        sum = 0
        result_list.append(tmp_list[0])
        for l in range(1, len(tmp_list)):
            sum = sum + int(tmp_list[l])
        result_list.append(sum)
        result_dict[result_list[0]] = result_list[1]
        result_list = []


print(f"Результат: {result_dict}")
print("Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие\n"
      "лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для\n"
      "каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета\n"
      "и общее количество занятий по нему. Вывести словарь на экран.")
from functools import reduce
tmp_list = []
count = 0
result_dict = {}
name = ""
result_list = []
with open("task-6.txt","r", encoding="utf-8") as f_obj:
    for i in f_obj:
        l = 0
        tmp_list = list(i.split())
        #print(tmp_list)
        tmp_list = [j.replace("(л)","") for j in tmp_list]
        tmp_list = [j.replace("(пр)", "") for j in tmp_list]
        tmp_list = [j.replace("(лаб).", "") for j in tmp_list]
        tmp_list = [j.replace("(лаб)", "") for j in tmp_list]
        #mp_list = [j.replace('—', "") for j in tmp_list]
        count = tmp_list.count("—")
        print(f"count {count}")
        for k in range(count):
            tmp_list = tmp_list[:tmp_list.index("—")]+tmp_list[tmp_list.index("—")+1:]

        sum = 0
        print(f"dfdasf {tmp_list}")
        result_list.append(tmp_list[0])
        print(f"result {result_list}")
        for l in range(1, len(tmp_list)):
            result_list.append(int(tmp_list[l]))
        sum = reduce(lambda acc, x: acc+x,result_list[1:])
        #result_list.append(map(int, tmp_list[1:]))
        print(f"result {result_list}")
        #result_dict.update(tmp_list)
        #result_dict[l] = tmp_list[0]
        #for k in range(1, len(tmp_list)):
            #result_dict[l].append(tmp_list[k])
        #l += 1


#print(f"словарь {result_dict}")

        #for j in range(len(i)):

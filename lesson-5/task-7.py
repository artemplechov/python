print("Задача 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:\n"
      "название, форма собственности, выручка, издержки.Необходимо построчно прочитать файл, вычислить прибыль каждой\n"
      "компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее\n"
      "реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.\n"
      "Если фирма получила убытки, также добавить ее в словарь (со значением убытков).Итоговый список сохранить в виде\n"
      "json-объекта в соответствующий файл")

import json

firms_dict = {}
firms_av_profit = {}
result_list = []
tmp_av_profit = 0
profit = 0
count = 0

with open("task-7.txt", "r", encoding = "utf-8") as f_obj:
    for string in f_obj:
        print(string)
        tmp_list = list(string.split())
        profit = (int(tmp_list[len(tmp_list)-2])-int(tmp_list[len(tmp_list)-1]))
        if profit > 0:
            tmp_av_profit += profit
            count += 1
        firms_dict[tmp_list[0]] = profit


av_profit = round(tmp_av_profit/count,2)
firms_av_profit = {'average_profit':av_profit}
result_list = [firms_dict,firms_av_profit]
print(f"Итоговый список: {result_list}")


with open("task-7_output.json", "w", encoding= "utf-8") as f_obj:
    json.dump(result_list,f_obj)
print("Задача 1. Создание скрипта, в котором предусмотрена функция\n"
      "расчета заработной платы. Скрипт необходимо запускать с параметрами.")
from sys import argv

script_name, first_param, second_param, third_param = argv

virabotka = int(first_param)
stavka = int(second_param)
premia = int(third_param)
print(f"Заработная плата сотрудника за месяц составила {(virabotka*stavka)+premia} у.е")
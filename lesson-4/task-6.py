print("Задача 6. Создание двух скриптов:\n"
      "а) итератор, генерирующий целые числа, начиная с указанного,\n"
      "б) итератор, повторяющий элементы некоторого списка, определенного заранее.")
import itertools

print("*******************Первый скрипт*******************")
for i in itertools.count(3):
    if i>=10:
        break
    else:
        print(i)

print("*******************Второй скрипт*******************")

j = 0
my_list = ["Hello!", "I'm learning Python!"]
for i in itertools.cycle(my_list):
    if j >= 10:
        break
    print(i)
    j += 1
print('Задание: Реализовать структуру "Рейтинг"')

my_list = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг: {my_list}")
my_list.append(int(input("Введите новый элемент рейтинга: ")))
my_list.sort()
my_list.reverse()
print(f"Обновленный рейтинг: {my_list}")
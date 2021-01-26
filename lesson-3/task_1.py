print("Задача 1: Создание функции деления с проверкой деления на 0")

correct = False

def delenie(a,b):
    s = a / b
    return s

while correct == False:
    chislitel = float(input("Введите числитель: "))
    znamenatel = float(input("Введите знаменатель: "))
    if znamenatel == 0:
        print("Внимание! Ошибка! На 0 делить нельзя. Повторите ввод!")
    else:
        correct = True

print(f"Результат деления: {delenie(chislitel,znamenatel):.2f}")

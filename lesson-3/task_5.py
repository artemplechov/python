print("Задача 5: Запрос у пользователя строки из чисел, разделенных пробелом, и сложение этих чисел")

summa = 0
spec_symbol = "q"
symbol_present = 0

def calculate(numbers, summa):
    for i in range(len(numbers)):
        summa += numbers[i]
    return summa

while symbol_present == 0:
    str_numbers = input("Введите последовательность цифр через пробел (для выхода нажмите q): ")
    if spec_symbol in str_numbers:
        str_numbers = str_numbers[:(str_numbers.index(spec_symbol))]
        numbers = list(map(int, str_numbers.split()))
        summa = calculate(numbers, summa)
        print(f"Сумма введенных чисел: {summa}")
        symbol_present = 1
    elif (str_numbers != spec_symbol) & (symbol_present == 0):
        numbers = list(map (int,str_numbers.split()))
        summa = calculate(numbers,summa)
        print(f"Сумма введенных чисел: {summa}")
    elif symbol_present != 0:
        break








print("\nПрограмма по поиску самой большой цифры в числе n\n")
n = input("Введите число n " )
length = len(n)
print(f"Длина n = {length}")
if int(n) > 0:
    max = int(n[0])
    for i in range(length-1):
        if max < int(n[i+1]):
            max = int(n[i+1])
    print(f"Максимальной цифрой в числе {n} является цифра {max}")
if int(n) < 0:
    print("Ошибка! Введите число больше 0!")



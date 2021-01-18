print("\nПрограмма по сложению n+nn+nnn\n")
str_single = input("Введите число n " )
summa = 0
for i in range(3):
    stroka = int(str_single*(i+1))
    summa += stroka
    print(stroka)
print(summa)
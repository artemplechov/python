print("Задание: Ввод строки из нескольких слов. Нумерация строк")

my_string = input("Введите строку: ")
j = 0
pos_of_whitespaces = []
for i in range(len(my_string)):
     if my_string[i] == ' ':
         pos_of_whitespaces.append(i)
for i in range(len(pos_of_whitespaces)):
    if len(my_string[j:pos_of_whitespaces[i]]) <= 10:
        print(f"строка №{i+1}: {my_string[j:pos_of_whitespaces[i]]}\n")
    else:
        print(f"строка №{i + 1}: {my_string[j:(j+10)]}\n")
    j = int(pos_of_whitespaces[i])+1
    if i == (len(pos_of_whitespaces)-1):
        print(f"строка №{i+2}: {my_string[pos_of_whitespaces[i]+1:len(my_string)]}\n")



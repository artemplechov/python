print("Задача 6: Ввод строки из слов, возврат строки со всеми словами с большой буквы")

def int_func(my_string):
    tmp_string = []
    result_string = ""
    list_of_words = my_string.split()
    for i in range(len(list_of_words)):
        tmp_string = list_of_words[i]
        tmp_string = chr(ord(tmp_string[:1]) - 32) + tmp_string[1:]
        result_string = result_string + " " + tmp_string
    return result_string[1:]

my_string = input("Введите строку. Слова в строке начинаются с\nпрописной буквы и разделяются пробелами:\n")
print(int_func(my_string))

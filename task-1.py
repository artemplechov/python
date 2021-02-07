print("Задание 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),\n"
      "который должен принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать\n"
      "перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__()\n"
      "для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть\n"
      "новая матрица.")

class Matrix:
    def __init__(self,total_list):
        self.list_zero = total_list[0]
        self.list_one = total_list[1]
        self.list_two = total_list[2]


    def __str__(self):
        my_str = ''
        #for i in range(3):
            #my_str += str(self.list_zero[i])+" "+str(self.list_one[i])+" "+str(self.list_two[i])+" \n"
        #my_str += str(self.list_zero) + "\n" + str(self.list_one) + "\n" + str(self.list_two)
        my_str = ("".join(str(self.list_zero)))+"\n"+("".join(str(self.list_one)))+"\n"+("".join(str(self.list_two)))
        return my_str

    def __add__(self,other):
        tmp_str_one = []
        tmp_str_two = []
        result = []
        my_str = ''
        for i in range(3):
            tmp_str_one.append(self.list_zero[i])
            tmp_str_one.append(self.list_one[i])
            tmp_str_one.append(self.list_two[i])
            tmp_str_two.append(other.list_zero[i])
            tmp_str_two.append(other.list_one[i])
            tmp_str_two.append(other.list_two[i])
        for i in range(9):
            result.append(tmp_str_one[i]+tmp_str_two[i])
        for i in range(0,9,3):
            my_str += str(result[i]) + " " + str(result[i+1]) + " " + str(result[i+2]) + " \n"
        print(tmp_str_one)
        print(tmp_str_two)
        print(result)
        return my_str







my_matrix_one = Matrix (([1,2,3], [4,5,6], [7,8,9]))
my_matrix_two = Matrix (([1,2,3], [4,5,6], [7,8,9]))

print(my_matrix_one)
print(my_matrix_two)
#print(my_matrix.list_one)
#print(my_matrix.list_two)
z = my_matrix_one+my_matrix_two
print(z)
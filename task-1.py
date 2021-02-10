print("Задание 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),\n"
      "который должен принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать\n"
      "перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__()\n"
      "для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть\n"
      "новая матрица.")

class Matrix:

    def __init__(self,total_list):
        matrix_list = []
        self.__total_list = total_list
        for i in range(len(self.__total_list)):
            for j in range(len(self.__total_list[0])):
                matrix_list.append(self.__total_list[i][j])
        self.__matrix_list = matrix_list



    def __str__(self):
        my_str = ''
        j = 0
        for i in range(len(self.__matrix_list)):
            if j !=(len(self.__total_list[0])):
                my_str += str(self.__matrix_list[i])+" "
                j += 1
            else:
                my_str += "\n"+str(self.__matrix_list[i])+" "
                j = 1
        return my_str

    def __add__(self,other):
        result = []
        my_str = ''
        j = 0
        for i in range(len(self.__matrix_list)):
            result.append(self.__matrix_list[i]+other.__matrix_list[i])
            if j !=(len(self.__total_list[0])):
                my_str += str(result[i])+" "
                j += 1
            else:
                my_str += "\n"+str(result[i])+" "
                j = 1
        return my_str

my_matrix_one = Matrix (([1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]))
my_matrix_two = Matrix (([1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]))

print(f"МАТРИЦА 1\n{my_matrix_one}")
print(f"МАТРИЦА 2\n{my_matrix_two}")
#
z = my_matrix_one+my_matrix_two
print(f"СУММА ДВУХ МАТРИЦ\n{z}")



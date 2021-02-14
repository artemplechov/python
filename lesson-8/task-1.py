print("Задание 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата\n"
      "«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать\n"
      "число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить\n"
      "валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных\n"
      "данных.")

class MyClassDate:

    @classmethod
    def convertstr(cls, str):
        date_list = []
        for value in (str.split('-')):
            date_list.append(int(value))
        return print(date_list)

    @staticmethod
    def valid(str):
        date_list = []
        for value in (str.split('-')):
            date_list.append(int(value))
        if (date_list[0] == 30 or date_list[0] == 31) and date_list[1] == 2:
            print("Ошибка ввода!В феврале только 28 или 29 дней!")
        elif 0 <= date_list[0] or date_list[0] > 31:
            print("Ошибка ввода! Количество дней в месяце должно быть в диапазоне от 1 до 31!")
        elif 0 <= date_list[1] > 12:
            print("Ошибка ввода! В году только 12 месяцев")
        else:
            print(date_list)




MyClassDate.convertstr("000-34-66")

z = MyClassDate
z.valid("10-13-2030")
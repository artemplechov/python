print("Задание 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу\n"
      "на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно\n"
      "обработать эту ситуацию и не завершиться с ошибкой.")

class OwnException:

     def __init__(self):
          self.a = 0
          self.b = 0

     def div(self):
         is_zero = False
         self.a = int(input("Введите числитель "))
         while not is_zero:
             try:
                self.b = int(input("Введите знаменатель "))
                self.z = self.a/self.b
                is_zero = True
             except ZeroDivisionError:
                 print("Знаменатель не можеть быть равен нулю. Повторите ввод!")
             else:
                 return self.z



a = OwnException()
print(a.div())
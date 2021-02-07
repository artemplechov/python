print('Задание 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position\n'
      '(должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий\n'
      'элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе\n' 
      'класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода\n' 
      'с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса\n'
      'Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).')

class Worker:
    _income = {"wage": None, "bonus": None}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def get_full_name(self):
        fio = self.name + " " + self.surname
        return print(f"ФИО: {fio}")

    def get_total_income(self, wage, bonus):
        sum = 0
        self._income["wage"] = wage
        self._income["bonus"] = bonus
        for value in self._income.values():
            sum += value
        return print(f"Доход с учетом премии: {sum}")
        pass

employee = Position("Иван", "Сидорович", "менеджер")
employee.get_full_name()
employee.get_total_income(100,50)


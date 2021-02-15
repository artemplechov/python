print("Задание 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс\n"
      "«Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер,\n"
      "сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках\n"
      "реализовать параметры, уникальные для каждого типа оргтехники.")


#
# class WareHouse():
#     def to_store(self,*goods):
#         for good in goods:
#
#     pass


class OffEquipment():
    def __init__(self, name, quantity):
        self.name = name #input("Оборудование: ")
        self.quantity = quantity #input("Количество: ")
       # self.list[self.name] =
       #  self.list = []
       #  self.list.append(self.name)
       #  self.list.append(self.quantity)
       #  self.list.append(self.addEquip)

class Printer(OffEquipment):
    def __init__(self, name, quantity, addEquip):
        super().__init__(name, quantity)
        self.addEquip = addEquip # addEquip #input("Дополнительные материалы (принтер - чернила): ")
        self.dic = {}
        self.dic[name] = self.quantity, self.addEquip
       # self.dic[name] = self.addEquip
    def __str__(self):
        return f"{self.name}, {self.quantity}, {self.addEquip}\n {self.dic}"



a = Printer("fdas", 5, "fadg")

print(a)


# my_dict = {"aaa": ( 5, "fdfa")}
# print(my_dict)
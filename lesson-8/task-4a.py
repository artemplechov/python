class OffEquipment:
    def __init__(self):
        self.name = input("Веедите товар: ")
        check = False
        while not check:
            try:
                self.quantity = int(input("Веедите количество: "))
                check = True
            except:
                print("Неверный ввод. Повторите еще раз!")


    def __str__(self):
        return f"{self.name} {self.quantity}"


class WareHouse():

    def to_store(*goods):
        my_dict = {}
        for key, value in goods:
            if key in my_dict.keys():
                my_dict[key] = my_dict[key]+value
            else:
                my_dict[key] = value
        return my_dict


class Printer(OffEquipment):
    def __init__(self):
        super().__init__()

    def return_func(self):
        self.list = []
        self.list.append(self.name)
        self.list.append(self.quantity)
        return self.list


s = WareHouse

p_1 = Printer()
p_2 = Printer()
p_3 = Printer()
p_4 = Printer()



a = p_1.return_func()
b = p_2.return_func()
c = p_3.return_func()
d = p_4.return_func()


print(f"Товары на складе: {s.to_store(a, b, c, d)}")


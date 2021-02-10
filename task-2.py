print("Задание 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность\n"
      "(класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте\n"
      "относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).\n"
      "Это могут быть обычные числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды\n"
      "использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на\n"
      "реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:\n"
      "реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.")


from abc import ABC, abstractmethod

class AbstractCloth(ABC):
    @abstractmethod
    def Square(self, v):
        pass

    def __add__(self, other):
        s = self.s+other.s
        return f"Общий расход ткани = {s}м"

class Coat(AbstractCloth):
    def __init__(self, v):
        self.v = v
        self.s = 0

    def Square(self):
        self.s = self.v/6.5 + 0.5
        return f"На пальто нужно {self.s}м ткани"


class Suit(AbstractCloth):
    def __init__(self, h):
        self.h = h
        self.s = 0

    def Square(self):
        self.s = 2*self.h + 0.3
        return f"На костюм нужно {self.s}м ткани"



my_coat = Coat(6.5)
my_suit = Suit(2)
print(my_coat.Square())
print(my_suit.Square())
z = my_suit+my_coat
print(z)
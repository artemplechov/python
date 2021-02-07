print("Задание 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)\n"
      "и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),\n"
      "Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из\n"
      "классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет\n"
      "описанный метод для каждого экземпляра.")


class Stationery:
    title = "канцелярская принадлежность"
    def draw(self):
        print("Запуск отрисовки!")


class Pen(Stationery):
    title = "ручка"
    def draw():
        print("Рисуем ручкой!")


class Pencil(Stationery):
    title = "карандаш"
    def draw():
        print("Рисуем карандашом!")


class Handle(Stationery):
    title = "марке"
    def draw():
        print("Рисуем маркером!")


my_pen = Pen
print(my_pen.title)
my_pen.draw()

my_pencil = Pencil
print(my_pencil.title)
my_pencil.draw()

my_handle = Handle
print(my_handle.title)
my_handle.draw()

my_stationery = Stationery
print(my_stationery.title)
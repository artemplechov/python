print("Задание 4. Реализуйте базовый класс Car. У класса должны быть следующие атрибуты: speed, color, name,\n"
      "is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,\n"
      "остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;\n"
      "добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов\n"
      "TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)\n"
      "должно выводиться сообщение о превышении скорости.")

import random

class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.colo = color
        self.name = name

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, directon):
        print(f"Машина повернула в{directon}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км\ч")

class TownCar(Car):
    def show_speed(self):
        if int(self.speed) >= 60:
            print(f"Внимание! Вы превысили скорость на {int(self.speed)-60} км\ч!!!\n"
                  f"Максимально разрешенная скорость 60 км\ч")
        else:
            print(f"Текущая скорость {self.speed} км\ч")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) >= 40:
            print(f"Внимание! Вы превысили скорость на {int(self.speed)-40} км\ч!!!\n"
                  f"Максимально разрешенная скорость 40 км\ч")
        else:
            print(f"Текущая скорость {self.speed} км\ч")

class PoliceCar(Car):
    is_police = True
    pass

car_type = input("Какая у Вас машина (городская, спорткар, грузовик, полиция): ").title()
speed = input("Ваша текущая скорость: ")
color = input("Цвет автомобиля: ")
name = input("Марка автомобиля: ")

if car_type == "Городская":
    my_car = TownCar(speed, color, name)
elif car_type == "Спорткар":
    my_car = SportCar(speed, color, name)
elif car_type == "Грузовик":
    my_car = WorkCar(speed, color, name)
elif car_type == "Полиция":
    my_car = PoliceCar(speed, color, name)
my_car.go()
my_car.show_speed()
my_car.turn(random.choice(["лево","право"]))
my_car.stop()
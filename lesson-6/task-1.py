print("Задание 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running\n"
      "(запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:\n"
      "красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)\n"
      "— 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в\n"
      "указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.")

import time

class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]
    def running(self):
        n = [7, 2, 1]
        for i in range(3):
            time.sleep(n[i])
            print(TrafficLight.__color[i])
        return


a = TrafficLight()
a.running()
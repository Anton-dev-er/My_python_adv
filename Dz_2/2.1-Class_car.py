"""
    ДОМАШНЕЕ ЗАДАНИЕ:
    1. Реализуйте базовый класс Car.
    У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
    40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Реализовать метод для user-friendly вывода информации об автомобиле.
"""


def main():
    print("=====Тест 1 =====")
    c = TownCar("Bmv", "Red", 70)
    c.stop()
    c.go(100)
    c.show_speed()
    c.go(10)
    c.turn("Ліво")
    print(c)

    print("\n\n=====Тест 2 =====")
    c1 = WorkCar("My_car", "Blue", 60)
    c1.stop()
    c1.go(50)
    c1.show_speed()
    c1.go(10)
    print(c1)


class Car:
    def __init__(self, name, color, speed):
        self._name = name
        self._color = color
        self._speed = speed

    def show_speed(self):
        print("Ваша швидкість", self._speed)

    def go(self, speed):
        if self._speed > speed:
            print(f"Ваша {self._name} сповільнюється до {speed} км/год")
        elif self._speed < speed:
            print(f"Ваша {self._name} розганяється до {speed} км/год")
        self._speed = speed

    def stop(self):
        print(f"Ваша {self._name} зупиняється")

    def turn(self, direction):
        print(f"Ваша {self._name} повернула на {direction}")

    def __str__(self):
        return f"Ваши данные:\n\tИмя:{self._name}, Цвет: {self._color}, Скорость:{self._speed}\n"


class TownCar(Car):
    def show_speed(self):
        super(TownCar, self).show_speed()
        if self._speed > 60:
            print("Ваша швидкість вище норми! Ваша швидкість знижена до 60")
            self._speed = 60


class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self._speed > 40:
            print("Ваша швидкість вище норми! Ваша швидкість знижена до 40")
            self._speed = 40


main()

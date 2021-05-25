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
    c = TownCar("Bmv", "Red", 70, 2012)
    c.stop()
    print("==")
    c.show_speed()
    print("==")
    c.go(100)
    print("==")
    c.show_speed()
    print("==")
    c.turn("Ліво")
    print("==")
    print(c)

    print("\n\n=====Тест 2 =====")
    c1 = WorkCar("My_car", "Blue", 60, 2021)
    c1.stop()
    c1.go(50)
    c1.show_speed()
    c1.go(10)
    print(c1)


class Car:
    _speed_limit = 0

    def __init__(self, name, color, speed):
        self._name = name
        self._color = color
        self._speed = speed

    def show_speed(self):
        print("Ваша скорость", self._speed)

    def go(self, speed):
        if self._speed > speed:
            print(f"Ваша {self._name} замедляется до {speed} км/год")
        elif self._speed < speed:
            print(f"Ваша {self._name} разгоняется до {speed} км/год")
        self._speed = speed

    def stop(self):
        print(f"Ваша {self._name} останавливается")
        self._speed = 0

    def turn(self, direction):
        print(f"Ваша {self._name} повернула на {direction}")


class TownCar(Car):
    __speed_limit = 60

    def __init__(self, name, color, speed, year):
        super().__init__(name, color, speed)
        self.__year = year

    def show_speed(self):
        super(TownCar, self).show_speed()
        if self._speed > __class__.__speed_limit:
            print("Ваша скорость выше нормы!")
            if input(f"Предлагаю снизить скорость до {__class__.__speed_limit} (y/n):") == "y":
                self._speed = __class__.__speed_limit

    def __str__(self):
        return f"Ваши данные:\n\tИмя:{self._name}, Цвет: {self._color}, Скорость:{self._speed},Год:{self.__year}\n"


class WorkCar(Car):
    __speed_limit = 60

    def __init__(self, name, color, speed, year):
        super().__init__(name, color, speed)
        self.__year = year

    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self._speed > __class__.__speed_limit:
            print("Ваша скорость выше нормы!")
            if input(f"Предлагаю снизить скорость до {__class__.__speed_limit} (y/n):") == "y":
                self._speed = __class__.__speed_limit

    def __str__(self):
        return f"Ваши данные:\n\tИмя:{self._name}, Цвет: {self._color}, Скорость:{self._speed},Год:{self.__year}\n"


main()

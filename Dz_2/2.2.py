"""
    2. Давайте представим, что мы занимаемся проектированием CRM для сервисного центра по обслуживанию и ремонту техники.
    Реализуйте класс Заявка. Каждая заявка должна иметь следующие поля: уникальный идентификатор (присваивается в момент)
    создания заявки автоматически, дата и время создания заявки (автоматически), имя пользователя, серийный номер
    оборудования, статус (активная заявка или закрытая например, статусов может быть больше). Id заявки сделать приватным
    полем.
    У заявки должны быть следующие методы:
    - метод, возвращающий, сколько заявка находится в активном статусе (если она в нём)
    - метод, изменяющий статус заявки
    - метод, возвращающий id заявки
"""
from datetime import date
import uuid


def main():
    c1 = Statement("Test1", "Test2", "Test3")
    c1.set_status()
    c1.show_data()
    c2 = Statement("Test1", "Test2", "Test3")
    c3 = Statement("Test1", "Test2", "Test3")
    c4 = Statement("Test1", "Test2", "Test3")
    c5 = Statement("Test1", "Test2", "Test3")
    print(Statement.get_count_status())


class Statement:
    __count_status = 0

    def __init__(self, name, serial_number, identificator, status="active"):
        self.__serial_number = serial_number
        self.__identificator = identificator
        self.__name = name
        self.__data = date.today()
        self.__status = status
        self.__ID = uuid.uuid4()
        Statement.__count_status += 1

    def set_status(self):
        a = input("Введите статус заявки active\closed: ")
        if a == "active":
            self.status = "active"
            print("Ваша заявка активная")
        elif a == "closed":
            self.status = "closed"
            print("Ваша заявка закрыта")
        else:
            self.status = "NonStatus"
            print("Ваша заявка без статусу")

    @staticmethod
    def get_count_status():
        return Statement.__count_status

    def get_id(self):
        return f"ID: {self.__ID}"

    def show_data(self):
        print(f"Name:{self.__name}\nSerial Number:{self.__serial_number}\nIdentificator:{self.__identificator}\
                \nStatus:{self.__status}\nID:{self.__ID}")


main()

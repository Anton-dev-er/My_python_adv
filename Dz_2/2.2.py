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
    c1.set_id()
    c1.show_data()
    c2 = Statement("Test1", "Test2", "Test3")
    c3 = Statement("Test1", "Test2", "Test3")
    c4 = Statement("Test1", "Test2", "Test3")
    c5 = Statement("Test1", "Test2", "Test3")
    print(Statement.get_count_status())


class Statement:
    __count_status = 0
    __id = "None"

    def __init__(self, name, serial_number, identificator, status="active"):
        self.serial_number = serial_number
        self.identificator = identificator
        self.name = name
        self.data = date.today()
        self.status = status
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
        return f"ID: {uuid.uuid4()}"

    def set_id(self):
        Statement.__id = uuid.uuid4()

    def show_data(self):
        print(f"Name:{self.name}\nSerial Number:{self.serial_number}\nIdentificator:{self.identificator}\
                \nStatus:{self.status}\nID:{Statement.__id}")


main()

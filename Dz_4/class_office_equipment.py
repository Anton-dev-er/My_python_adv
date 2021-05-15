from abc import ABC, abstractmethod
import string
import random


class OfficeEquipment(ABC):
    @abstractmethod
    def start_work(self):
        pass

    @abstractmethod
    def finish_work(self):
        pass

    @abstractmethod
    def show_info(self):
        pass


class Printer(OfficeEquipment):
    __start_button = False
    __cartridge = False

    def __init__(self, model, year):
        self.model = model
        self.__year = year
        self.__serial_number = ''.join(random.choice(string.ascii_letters) for x in range(5))

    def set_cartridge(self):
        if self.__start_button == True:
            print("Нельзя выполнить когда включен принтер")
        else:
            print("Картредж установлен")
            self.__cartridge = True

    def start_work(self, picture):
        print("Начало работы")
        self.__start_button = True
        if self.__cartridge == False:
            print("Ошибка,установите картредж!!")
            print(f"Нельзя напечатать:{picture}")
        else:
            print(f"{picture} Успешно напечатан")

    def finish_work(self):
            print("Конец работы")
            self.__start_button = False

    def show_info(self):
        print(f"Model:{self.model}\nYear:{self.__year}\nSerial number:{self.__serial_number}")


class Scanner(OfficeEquipment):
    __start_button = False

    def __init__(self, model, year, format_):
        self.model = model
        self.__year = year
        self.__format_ = format_
        self.__serial_number = ''.join(random.choice(string.ascii_letters) for x in range(5))

    def start_scan(self, document):
        if self.__start_button == False:
            print("Включите сканер")
        else:
            print(f"вы просканировали:{document}")

    def start_work(self):
        print("Начало работы")
        self.__start_button = True

    def finish_work(self):
        print("Конец работы")
        self.__start_button = False

    def show_info(self):
        print(f"Model:{self.model}\nYear:{self.__year}\nFormat:{self.__format_}\nSerialNumber:{self.__serial_number}")


class Xerox(OfficeEquipment):
    __start_button = False

    def __init__(self, model, year):
        self.model = model
        self.__year = year
        self.__serial_number = ''.join(random.choice(string.ascii_letters) for x in range(5))

    def start_xerox(self, document):
        if self.__start_button == False:
            print("Включите ксерокс")
        else:
            print(f"Вы сделали ксерокопию:{document}")

    def start_work(self):
        print("Начало работы")
        self.__start_button = True

    def finish_work(self):
        print("Конец работы")
        self.__start_button = False

    def show_info(self):
        print(f"Model:{self.model}\nYear:{self.__year}\nSerialNumber:{self.__serial_number}")


class Warehouse:
    @staticmethod
    def show_info(device):
        if isinstance(device, list):
            for i in device:
                print("\n\t" + i.model)
                i.show_info()
        else:
            device.show_info()

    def __init__(self, items):
        self.items = items

    # def __getitem__(self, index):
    #     return self.items[index]

    def __iter__(self):
        return iter(self.items)

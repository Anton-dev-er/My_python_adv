from abc import ABC, abstractmethod
import string
import random


class OfficeEquipment(ABC):
    @abstractmethod
    def start_work(self, item):
        pass

    @abstractmethod
    def finish_work(self):
        pass

    @abstractmethod
    def show_info(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, model, year):
        self.model = model
        self.__year = year
        self.__serial_number = ''.join(random.choice(string.ascii_letters) for x in range(5))
        self.__start_button = False
        self.__cartridge = False

    def set_cartridge(self):
        if self.__cartridge == True:
            print("Картредж уже установлен")
        else:
            print("Картредж установлен")
            self.__cartridge = True

    def start_work(self, paper_for_print):
        print("Начало работы")
        self.__start_button = True
        if self.__cartridge == False:
            print("Ошибка,установите картредж!!")
            print(f"Нельзя напечатать:{paper_for_print}")
        else:
            print(f"{paper_for_print} Успешно напечатан")

    def finish_work(self):
        print("Конец работы")
        self.__start_button = False

    def show_info(self):
        print(f"Model:{self.model}\nYear:{self.__year}\nSerial number:{self.__serial_number}")


class Scanner(OfficeEquipment):
    def __init__(self, model, year, format_):
        self.model = model
        self.__year = year
        self.__format_ = format_
        self.__serial_number = ''.join(random.choice(string.ascii_letters) for x in range(5))
        self.__start_button = False

    def start_work(self, paper_for_scan):
        print("Начало работы")
        self.__start_button = True
        if self.__start_button == False:
            print("Включите сканер")
        else:
            print(f"вы просканировали:{paper_for_scan}")

    def finish_work(self):
        print("Конец работы")
        self.__start_button = False

    def show_info(self):
        print(f"Model:{self.model}\nYear:{self.__year}\nFormat:{self.__format_}\nSerialNumber:{self.__serial_number}")


class Xerox(OfficeEquipment):
    def __init__(self, model, year):
        self.model = model
        self.__year = year
        self.__serial_number = ''.join(random.choice(string.ascii_letters) for x in range(5))
        self.__start_button = False

    def start_work(self, paper_for_xerox):
        print("Начало работы")
        self.__start_button = True
        if self.__start_button == False:
            print("Включите ксерокс")
        else:
            print(f"Вы сделали ксерокопию:{paper_for_xerox}")

    def finish_work(self):
        print("Конец работы")
        self.__start_button = False

    def show_info(self):
        print(f"Model:{self.model}\nYear:{self.__year}\nSerialNumber:{self.__serial_number}")


class Warehouse:
    def __init__(self):
        self.__devices = []

    def __iter__(self):
        return iter(self.__devices)

    def show_devices(self):
        for i in self.__devices:
            print("\n\t" + i.model)
            i.show_info()

    def equipment_add_to_warehouse(self, device):
        self.__devices.append(device)

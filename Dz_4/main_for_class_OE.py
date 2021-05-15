from class_office_equipment import *


def main():

    pr = Printer("Asus", 2002)
    pr.set_cartridge()
    pr.start_work("Рисунок")
    print("\n=================")
    scan = Scanner("Philips", 2020, "A4")
    scan.start_work()
    scan.start_scan("Документ")
    print("\n=================")
    xerox = Xerox("Xerox ", 2020)
    xerox.start_work()
    xerox.start_xerox("Паспорт")
    print("\n=================")

    print("\n\ntest 1")
    device = []
    device.append(scan)
    device.append(pr)
    device.append(xerox)
    Warehouse.show_info(device)
    print("\n\ntest 2")
    Warehouse.show_info(Printer("MyPrinter", 2020))

    print("\n\ntest 3")
    for i in Warehouse(device):
        print(i)


main()
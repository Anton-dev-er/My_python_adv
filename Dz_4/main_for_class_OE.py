from class_office_equipment import *


def main():
    pr = Printer("Asus", 2002)
    pr.set_cartridge()
    pr.set_cartridge()
    pr.start_work("Рисунок")
    print("\n=================")
    scan = Scanner("Philips", 2020, "A4")
    scan.start_work("Документ")
    print("\n=================")
    xerox = Xerox("Xerox ", 2020)
    xerox.start_work("Паспорт")

    print("\n\n=====Test 1=====")
    w = Warehouse()
    w.equipment_add_to_warehouse(pr)
    w.equipment_add_to_warehouse(xerox)
    w.equipment_add_to_warehouse(scan)
    w.show_devices()

    print("\n\n=====Test 2=====")
    for i in w:
        print(i.model)


main()
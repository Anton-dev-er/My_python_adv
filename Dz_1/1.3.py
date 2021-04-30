def func():
    while True:
        try:
            n1, n2, n3 = input("Введіть 3 числа: ").split()
            return int(n1) + int(n2) + int(n3) - min([int(n1), int(n2), int(n3)])
        except:continue


print(func())

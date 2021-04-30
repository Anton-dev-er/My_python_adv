#1, 1, 2, 3, 5, 8, 13 ...
i = int(input("Введите номер элемента числа:"))
f2 = 1
a = 0
number = 0
while a < i:
    f1 = f2
    f2 = number
    number = f2 + f1
    a += 1
print(number)
sum_number = 0
while True:
    numbers = [i for i in input("Введите числа через пробел:").split()]
    for number in numbers:
        if number.isdigit():
            sum_number += int(number)
        else:
            break
    print(sum_number)
    if input("Continue(y/n):") == "n":break
            
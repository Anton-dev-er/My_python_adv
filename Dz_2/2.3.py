""""
3. Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список. Для объектов
класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы на число и user-friendly вывода
матрицы на экран.
"""

import random

# Сделал все хард кодом если нужно то переделаю
def main():
    l_matrix = []
    print("Test 1")
    for i in range(0, 3):
        l_matrix.append([int(random.randint(10, 20)) for i in range(0, 3)])
    m1 = Matrix(l_matrix)
    print(m1)

    print("\nTest 2")
    m2 = Matrix(l_matrix)
    print(m2)

    print("\nTest 3")
    print(m1 + m2)
    print(m1 - m2)
    print(m1 * 100)
    print(m1 / 100)


class Matrix:
    def __init__(self, list_matrix):
        self.list_matrix = list_matrix

    def __add__(self, other):
        new_matrix = [[0]*3 for i in range(3)]
        if len(self.list_matrix) == len(other.list_matrix):
            for i in range(3):
                for j in range(3):
                    new_matrix[i][j] = self.list_matrix[i][j] + other.list_matrix[i][j]
            return Matrix(new_matrix)
        else:
            return "Error"

    def __sub__(self, other):
        new_matrix = [[0]*3 for i in range(3)]
        if len(self.list_matrix) == len(other.list_matrix):
            for i in range(3):
                for j in range(3):
                    new_matrix[i][j] = self.list_matrix[i][j] - other.list_matrix[i][j]
            return Matrix(new_matrix)
        else:
            return "Error"

    def __mul__(self, number):
        new_matrix = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                new_matrix[i][j] = self.list_matrix[i][j] * number
        return Matrix(new_matrix)

    def __truediv__(self, number):
        new_matrix = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                new_matrix[i][j] = self.list_matrix[i][j] / number
        return Matrix(new_matrix)

    def __str__(self):
        return f"Ваш список:{(' '.join(map(str, self.list_matrix)))}"



main()
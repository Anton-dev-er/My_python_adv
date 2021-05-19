""""
3. Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список. Для объектов
класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы на число и user-friendly вывода
матрицы на экран.
"""

import random


def main():
    l_matrix = []
    height = int(input("Введите высоту"))
    width = int(input("Введите ширину"))
    print("Test 1")
    for i in range(0, height):
        l_matrix.append([int(random.randint(10, 20)) for i in range(0, width)])
    m1 = Matrix(l_matrix)
    m1.set_side(height, width)
    print(m1)

    print("\nTest 2")
    m2 = Matrix(l_matrix)
    m2.set_side(height, width)
    print(m2)

    print("\nTest 3")
    print(m1 + m2)
    print(m1 - m2)
    print(m1 * 100)
    print(m1 / 100)


class Matrix:
    height, width = 0, 0

    def __init__(self, list_matrix):
        self.list_matrix = list_matrix

    def set_side(self, height, width):
        self.height = height
        self.width = width

    def __add__(self, other):
        new_matrix = [[0] * self.width for i in range(self.height )]
        if len(self.list_matrix) == len(other.list_matrix):
            for i in range(self.height):
                for j in range(self.width):
                    new_matrix[i][j] = self.list_matrix[i][j] + other.list_matrix[i][j]
            return Matrix(new_matrix)
        else:
            raise ValueError("Wrong value")

    def __sub__(self, other):
        new_matrix = [[0] * self.width for i in range(self.height )]
        if len(self.list_matrix) == len(other.list_matrix):
            for i in range(self.height):
                for j in range(self.width):
                    new_matrix[i][j] = self.list_matrix[i][j] - other.list_matrix[i][j]
            return Matrix(new_matrix)
        else:
            raise ValueError("Wrong value")

    def __mul__(self, number):
        new_matrix = [[0] * self.width for i in range(self.height )]
        for i in range(self.height):
            for j in range(self.width):
                new_matrix[i][j] = self.list_matrix[i][j] * number
        return Matrix(new_matrix)

    def __truediv__(self, number):
        new_matrix = [[0] * self.width for i in range(self.height )]
        for i in range(self.height):
            for j in range(self.width):
                new_matrix[i][j] = self.list_matrix[i][j] / number
        return Matrix(new_matrix)

    def __str__(self):
        return f"Ваш список:{(' '.join(map(str, self.list_matrix)))}"


main()
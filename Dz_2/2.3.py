import random


def main():
    l_matrix = []
    height = int(input("Введите высоту:"))
    width = int(input("Введите ширину:"))
    print("Test 1")
    for i in range(0, height):
        l_matrix.append([int(random.randint(10, 20)) for i in range(0, width)])
    m1 = Matrix(l_matrix)
    print(m1)

    print("\nTest 2")
    m2 = Matrix(l_matrix)


    print(m1 + m2)
    print(m1 - m2)
    print(m1 * 100)
    print(m1 / 100)


class Matrix:
    def __init__(self, list_matrix):
        self.list_matrix = list_matrix
        self.height = len(list_matrix)
        self.width = len(list_matrix[0])
        self.new_matrix = [[0] * self.width for i in range(self.height)]

    def __add__(self, other):
        if len(self.list_matrix) == len(other.list_matrix):
            for i in range(self.height):
                for j in range(self.width):
                    self.new_matrix[i][j] = self.list_matrix[i][j] + other.list_matrix[i][j]
            return Matrix(self.new_matrix)
        else:
            raise ValueError("Wrong value")

    def __sub__(self, other):
        if len(self.list_matrix) == len(other.list_matrix):
            for i in range(self.height):
                for j in range(self.width):
                    self.new_matrix[i][j] = self.list_matrix[i][j] - other.list_matrix[i][j]
            return Matrix(self.new_matrix)
        else:
            raise ValueError("Wrong value")

    def __mul__(self, number):
        for i in range(self.height):
            for j in range(self.width):
                self.new_matrix[i][j] = self.list_matrix[i][j] * number
        return Matrix(self.new_matrix)

    def __truediv__(self, number):
        for i in range(self.height):
            for j in range(self.width):
                self.new_matrix[i][j] = self.list_matrix[i][j] / number
        return Matrix(self.new_matrix)

    def __str__(self):
        return f"Ваш список:{(' '.join(map(str, self.list_matrix)))}"


main()
import random

class Matrix:
    def __init__(self, list_matrix):
        self.list_matrix = list_matrix
        self.height = len(list_matrix)
        self.width = len(list_matrix[0])

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


def test_():
    assert Matrix([2, 2]) == Matrix([2, 2])



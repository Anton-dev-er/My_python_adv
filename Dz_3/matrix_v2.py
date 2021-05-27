
class Matrix:
    def __init__(self, list_matrix):
        self.__list_matrix = list_matrix
        self.__height = len(self.__list_matrix)
        self.__width = len(self.__list_matrix[0])
        self.__new_matrix = [[0] * self.__width for i in range(self.__height)]

    def matrix_data(self):
        return self.__list_matrix

    def __add__(self, other):
        if len(self.__list_matrix) == len(other.__list_matrix):
            for i in range(self.__height):
                for j in range(self.__width):
                    self.__new_matrix[i][j] = self.__list_matrix[i][j] + other.__list_matrix[i][j]
            return Matrix(self.__new_matrix)
        else:
            raise ValueError("Wrong value")

    def __sub__(self, other):
        if len(self.__list_matrix) == len(other.__list_matrix):
            for i in range(self.__height):
                for j in range(self.__width):
                    self.__new_matrix[i][j] = self.__list_matrix[i][j] - other.__list_matrix[i][j]
            return Matrix(self.__new_matrix)
        else:
            raise ValueError("Wrong value")

    def __mul__(self, number):
        for i in range(self.__height):
            for j in range(self.__width):
                self.__new_matrix[i][j] = self.__list_matrix[i][j] * number
        return Matrix(self.__new_matrix)

    def __truediv__(self, number):
        for i in range(self.__height):
            for j in range(self.__width):
                self.__new_matrix[i][j] = self.__list_matrix[i][j] / number
        return Matrix(self.__new_matrix)

    def __str__(self):
        return f"Ваш список:{(' '.join(map(str, self.__list_matrix)))}"


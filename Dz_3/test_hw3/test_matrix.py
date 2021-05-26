class Matrix:
    def __init__(self, list_matrix):
        self.list_matrix = list_matrix
        self.new_matrix = list_matrix
        try:
            self.height = len(list_matrix)
            self.width = len(list_matrix[0])
        except:
            self.height = 0
            self.width = len(list_matrix)

        print(self.width, self.height)

    def __add__(self, other):
        if self.width == other.width and self.height == other.height:
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


print(Matrix([1, 1]) * 5)
# print(Matrix([1, 1]) + Matrix([1, 1]))
# def test_m():
#     assert str(Matrix([1, 1, 1])) == str(Matrix([1, 1, 1]))
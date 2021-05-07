import random


class Matrix:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.matrix = list()
        for i in range(0, height):
            self.matrix.append([int(random.randint(10, 80)) for i in range(0, weight)])

    def show_matrix(self):
        for i in range(self.height):
            print(i, "", " ".join(map(str, self.matrix[i])))

    def __add__(self, number):
        for i in range(self.height):
            for j in range(self.weight):
                self.matrix[i][j] = self.matrix[i][j] + number
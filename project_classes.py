import numpy as np


class UserInput:
    def __init__(self):
        self.C = None  # A vector of coefficients of objective function
        self.A = None  # A matrix of coefficients of constraint function
        self.b = None  # A vector of right-hand side numbers
        self.a = None  # The approximation accuracy
        self.size = []

    def input_size(self):
        self.size = list(map(int, input("Write size of matrix (ex: 4 5): ").split()))

    def input_C(self):
        self.C = list(map(int, input("Write C (ex: 2 3 0 0 4): ").split()))

    def input_A(self):
        self.A = []
        print("Write A:\nex: 4 5 6\n    5 1 2")
        for i in range(self.size[0]):
            line = list(map(int, input().split()))
            self.A.append(line)

    def input_b(self):
        self.b = list(map(int, input("Write b: ").split()))

    def input_a(self):
        self.a = int(input("Write accuracy: "))


class SimplexMethod:
    def __init__(self, size, C, A, b, a):
        self.size = size  # size of A
        self.C = np.array(C)  # A vector of coefficients of objective function
        self.A = np.array(A)  # A matrix of coefficients of constraint function
        self.b = np.array(b)  # A vector of right-hand side numbers
        self.a = np.array(a)  # The approximation accuracy.
        self.B = np.array([[0 for j in range(self.size[0])] for i in range(self.size[0])])  # basis
        self.B_indexes = [0 for i in range(self.size[0])]  # indexes of basis

    def main(self):
        self.find_basic_variables()
        B_inverse = self.B.transpose()
        #algorithm
        # loop

    def find_basic_variables(self):
        for i in range(self.size[0]):
            basis = np.array([0 for i in range(self.size[0])])
            basis[i] = 1
            for j in range(self.size[1]):
                if np.array_equal(self.A[:, j], basis.transpose()):
                    self.B[i][i] = 1
                    self.B_indexes[i] = j

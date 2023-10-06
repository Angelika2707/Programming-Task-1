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
        self.X_b = np.zeros((1, self.size[0]))      # optimal solution vector
        self.z = 0  # optimal value
        self.C_b = np.zeros((1, self.size[0]))  # values of non-basic variables in C
        self.non_basis = [0] * (self.size[1] - self.size[0])    # A vector of non-basic variables

    def main(self):
        self.find_basic_variables()
        self.find_non_basic_variables()
        B_inversed = np.linalg.inv(self.B)
        entering_vector_inx = self.compute_optimality(B_inversed)

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

    def find_non_basic_variables(self):
        j = 0
        for i in range(self.size[0]):
            if not(i in self.B_indexes):
                self.non_basis[j] = i
                j += 1

    # return index of entering vector P_j
    # with new iteration basis B and indexes is changed
    # elements in C also changed
    def compute_optimal_solution(self, B_inversed):
        b_transposed = self.b.transpose()
        self.X_b = (B_inversed.dot(b_transposed))
        self.z = self.C_b.dot(self.X_b.transpose())

    def compute_optimality(self, B_inversed):
        self.compute_optimal_solution(B_inversed)
        cur_size = self.size[1] - self.size[0]  # number of non-basic variables
        z = [0 for i in range(cur_size)]
        temp_product = self.C_b.dot(B_inversed)
        flag = False
        for i in range(cur_size):
            z[i] = temp_product.dot(self.A[:, self.non_basis[i]]) - self.C.transpose()[self.non_basis[i]]
            print(z[i])
            if z[i] >= 0:
                flag = True

        if flag:
            return
            # deliver self.X_b and self.z to output
        else:
            min_neg_el = np.min(z)
            j = z.index(min_neg_el)  # index of entering vector Pj
            print(self.non_basis[j])
        return self.non_basis[j]



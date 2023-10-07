import numpy as np


class UserInput:
    def __init__(self):
        self.C = None  # A vector of coefficients of objective function
        self.A = None  # A matrix of coefficients of constraint function
        self.b = None  # A vector of right-hand side numbers
        self.a = None  # The approximation accuracy
        self.size = []

    def collect_data(self):
        self.input_size()
        self.input_C()
        self.input_A()
        self.input_b()
        self.input_a()

    def input_size(self):
        self.size = list(map(int, input("Enter the size of matrix A (example: 4 5): ").split()))

    def input_C(self):
        self.C = list(map(int, input("Enter vector C (ex: 2 3 0 0 4): ").split()))

    def input_A(self):
        self.A = []
        print("Enter matrix A:\nexample: 4 5 6\n         5 1 2")
        for i in range(self.size[0]):
            line = list(map(int, input().split()))
            self.A.append(line)

    def input_b(self):
        self.b = list(map(int, input("Enter vector b: ").split()))

    def input_a(self):
        self.a = int(input("Enter approximation accuracy: "))


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
        self.C_b = np.zeros((self.size[0]))  # values of non-basic variables in C
        self.non_basis = [0] * (self.size[1] - self.size[0])    # A vector of non-basic variables (indexes)

    def revised_simplex_method(self):
        self.find_basic_variables()
        self.find_non_basic_variables()
        B_inversed = np.linalg.inv(self.B)

        while True:
            entering_vector_inx = self.compute_optimality(B_inversed)

            if entering_vector_inx is None:
                result = np.append([self.z], np.zeros(self.size[1]))
                j = 0
                for i in self.B_indexes:
                    result[i + 1] = self.X_b[j]
                    j += 1
                return result

            B_inv_P_j = B_inversed.dot(self.A[:, entering_vector_inx])

            # check for unbounded solutions
            if all(v <= 0 for v in B_inv_P_j):
                return None

            leaving_vector_index = self.determine_leaving_vector(B_inv_P_j)

            entering_var_index = self.non_basis.index(entering_vector_inx)
            temp = self.non_basis[entering_var_index]
            self.non_basis[entering_var_index] = self.B_indexes[leaving_vector_index]
            self.B_indexes[leaving_vector_index] = temp
            self.B[:, leaving_vector_index] = self.A[:, entering_vector_inx]
            B_inversed = np.linalg.inv(self.B)
            self.C_b[leaving_vector_index] = self.C[self.B_indexes[leaving_vector_index]]

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
        count = 0
        for i in range(cur_size):
            z[i] = temp_product.dot(self.A[:, self.non_basis[i]]) - self.C.transpose()[self.non_basis[i]]
            print(z[i])
            if z[i] >= 0:
                count += 1

        if count == cur_size:
            return None
        else:
            min_neg_el = np.min(z)
            j = z.index(min_neg_el)  # index of entering vector Pj
            print(self.non_basis[j])
        return self.non_basis[j]

    def determine_leaving_vector(self, B_inv_P_j):
        min_ratio = float('inf')
        leaving_vector_index = None

        for i in range(self.size[0]):
            if B_inv_P_j[i] != 0:
                ratio = self.X_b[i] / B_inv_P_j[i]
                if min_ratio > ratio > 0:
                    min_ratio = ratio
                    leaving_vector_index = i
        return leaving_vector_index

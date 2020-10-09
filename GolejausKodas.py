import numpy as np


class Duomenys:
    def __init__(self, I, B, G):
        self.I = I
        self.B = B
        self.G = G

    def zeros_matrix(self, rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0)

        return M

    def identity_matrix(self, n):
        IdM = self.zeros_matrix(n, n)
        for i in range(n):
            IdM[i][i] = 1

        return IdM

    def matrix_multiply(self, A, B):
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])
        if colsA != rowsB:
            raise ArithmeticError(
                'Number of A columns must equal number of B rows.')

        C = self.zeros_matrix(rowsA, colsB)
        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for ii in range(colsA):
                    total += A[i][ii] * B[ii][j]
                C[i][j] = total

        return C


if __name__ == '__main__':

    # B = [
    #     [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    #     [1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0],
    #     [0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0],
    #     [1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0],
    #     [1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0],
    #     [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0],
    #     [0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0],
    #     [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0],
    #     [0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0],
    #     [1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
    #     [0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0],  # 11
    #     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]

    B = [
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],  # 11
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    I = []
    G = []

    duomenys = Duomenys(I, B, G)
    duomenys.I = duomenys.identity_matrix(12)

    G = duomenys.zeros_matrix(12, 23)
    for j in range(len(duomenys.I)):
        row = duomenys.I[j] + duomenys.B[j]
        G[j] = row

    duomenys.G = G

    print(G)

#---------------------------------------------------------------------------- Kodavimas

    user_input = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1,
                  1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1]

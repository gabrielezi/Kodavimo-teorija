import numpy as np
import random


class Veiksmai:

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
                C[i][j] = total % 2

        return C

    def siustiKanalu(self, vekt, p):
        gaunamasVekt = self.zeros_matrix(1, len(vekt[0]))

        for i in range(len(vekt[0])):
            a = random.random()
            if a < p:
                gaunamasVekt[0][i] = (vekt[0][i]+1) % 2
            else:
                gaunamasVekt[0][i] = vekt[0][i]

        return gaunamasVekt

    def uzkoduotiVektoriu(self, vekt, G):
        return self.matrix_multiply(vekt, G)

    def matrix_addition(self, A, B):
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])
        if rowsA != rowsB or colsA != colsB:
            raise ArithmeticError('Matrices are NOT the same size.')

        # Section 2: Create a new matrix for the matrix sum
        C = self.zeros_matrix(rowsA, colsB)

        # Section 3: Perform element by element sum
        for i in range(rowsA):
            for j in range(colsB):
                C[i][j] = (A[i][j] + B[i][j]) % 2

        return C

    def vectorE(self, i):
        a = self.zeros_matrix(1, 12)
        a[0][i] = 1
        return a

    def findDifferences(self, original, modified):
        differences = []

        for i in range(len(original[0])):
            if modified[0][i] != original[0][i]:
                differences.append(i)
        return differences

    def stringToBinary(self, text):
            res = ' '.join(format(ord(x), 'b') for x in text)
            return res

    def skaidytiBinary(self, text):
            binary_values = text.split()
            skaidList = []
            addedZeros = []
            for binary_value in binary_values:
                integer = binary_value
                for _ in range(12-len(binary_value)):
                    integer = integer + "0"
                addedZeros.append(12-len(binary_value))
                skaidList.append(int(integer))
            return skaidList, addedZeros
            

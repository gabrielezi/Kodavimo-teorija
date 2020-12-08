import numpy as np
import random

class Veiksmai:
# Funkcija nulinei matricai sudaryti.
# Paduodamos eilutės ir stulpeliai, grąžinama sudaryta matrica.
    def zeros_matrix(self, rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0)
        return M

# Funkcija vienetinei matricai sudaryti.
# Paduodamas skaičius eilučių ir stulpelių, grąžinama sudaryta kvadratinė matrica.
    def identity_matrix(self, n):
        IdM = self.zeros_matrix(n, n)
        for i in range(n):
            IdM[i][i] = 1
        return IdM

# Matricų daugybos funkcija.
# Paduodamas dvi matricos, grąžinama viena sudauginta matrica.
    def matrix_multiply(self, A, B):
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])
        if colsA != rowsB:
            raise ArithmeticError(
                'A matricos stulpeliu skaicius turi buti lygus B eiluciu skaiciui.')

        C = self.zeros_matrix(rowsA, colsB)
        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for ii in range(colsA):
                    total += A[i][ii] * B[ii][j]
                C[i][j] = total % 2
        return C

# Matricų sudėtis.
# Paduodamas dvi matricos, grąžinama sudėta matrica.
    def matrix_addition(self, A, B):
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])
        if rowsA != rowsB or colsA != colsB:
            raise ArithmeticError('Matricos NERA vienodo dydzio.')

        C = self.zeros_matrix(rowsA, colsB)

        for i in range(rowsA):
            for j in range(colsB):
                C[i][j] = (A[i][j] + B[i][j]) % 2

        return C

# Vektorius e -  12-os dydžio vektorius su vienetu i-tojoje pozicijoje
# Paduodama i-toji pozicija, grąžinamas e vektorius.
    def vectorE(self, i):
        a = self.zeros_matrix(1, 12)
        a[0][i] = 1
        return a

    

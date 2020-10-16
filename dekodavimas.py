import numpy as np
import random
from veiksmai import Veiksmai


class Dekodavimas:

    def __init__(self, H, sind, svoris):
        self.H = H
        self.sind = sind
        self.svoris = svoris

    def makeNelyginisVekt(self, vekt):
        suma = sum(vekt[0])
        if suma % 2 == 0:
            return [vekt[0] + [1]]
        else:
            return [vekt[0] + [0]]

    def sindromas(self, vekt):
        veiksmai = Veiksmai()
        self.sind = veiksmai.matrix_multiply(vekt, self.H)
        # print("sindromas: ", self.sind)

    def calcKlaidos(self, B):
        veiksmai = Veiksmai()
        u = []
        self.svoris = sum(self.sind[0])
        # print('svoris: ', self.svoris)
        if self.svoris <= 3:
            u = self.sind[0] + veiksmai.zeros_matrix(1, 12)[0]
        else:
            for i in range(len(B)):
                sumSB = veiksmai.matrix_addition(self.sind, [B[i]])
                if sum(sumSB[0]) <= 2:
                    u = sumSB[0] + veiksmai.vectorE(i)[0]
            if u == []:
                sind2 = veiksmai.matrix_multiply(self.sind, B)
                svoris2 = sum(sind2[0])
                if svoris2 <= 3:
                    u = veiksmai.zeros_matrix(1, 12)[0] + sind2[0]
                else:
                    for i in range(len(B)):
                        sumSB2 = veiksmai.matrix_addition(sind2, [B[i]])
                        if sum(sumSB2[0]) <= 2:
                            u = veiksmai.vectorE(i)[0] + sumSB2[0]
                    if u == []:
                        print("atsiuskite vektoriu is naujo")

        return u

    def dekoduoti(self, gautasVekt, B12):
        veiksmai = Veiksmai()
        nelyginisVekt = self.makeNelyginisVekt(gautasVekt)

        self.sindromas(nelyginisVekt)

        u = self.calcKlaidos(B12)

        v = veiksmai.matrix_addition(nelyginisVekt, [u])

        result = v[0][:12]

        return result

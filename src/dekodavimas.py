import numpy as np
import random
from veiksmai import Veiksmai
from duomenys import Duomenys

class Dekodavimas:

    def __init__(self, sind, svoris):
        duomenys = Duomenys()
        self.H = duomenys.I + duomenys.B12
        self.sind = sind
        self.svoris = svoris
        self.B12 = duomenys.B12
        self.veiksmai = Veiksmai()

# Nurodyto vektoriaus gale pridedamas 0 arba 1, taip, kad 
# vektoriaus svoris būtų nelyginis skaičius.
# Paduodamas 23-ų ilgio vektorius, grąžinamas 24-ių ilgio vektorius.
    def makeNelyginisVekt(self, vekt):
        suma = sum(vekt[0])
        if suma % 2 == 0:
            return [vekt[0] + [1]]
        else:
            return [vekt[0] + [0]]

# Skaičiuojamas sindromas dauginant 24-ių ilgio vektorių ir matricą H(24x12)
# Paduodamas 24-ių ilgio vektorius, gaunamas vektorius ilgio 12
    def sindromas(self, vekt):
        self.sind = self.veiksmai.matrix_multiply(vekt, self.H)

# 3.6.1 Algoritmas, išskyrus sindromo skaičiavimą.
# Grąžinamas u klaidų vektorius.
    def calcKlaidos(self):
        u = []
        self.svoris = sum(self.sind[0])
        if self.svoris <= 3:
            u = self.sind[0] + self.veiksmai.zeros_matrix(1, 12)[0]
        else:
            for i in range(len(self.B12)):
                sumSB = self.veiksmai.matrix_addition(self.sind, [self.B12[i]])
                if sum(sumSB[0]) <= 2:
                    u = sumSB[0] + self.veiksmai.vectorE(i)[0]
                    break
            if u == []:
                sind2 = self.veiksmai.matrix_multiply(self.sind, self.B12)
                svoris2 = sum(sind2[0])
                if svoris2 <= 3:
                    u = self.veiksmai.zeros_matrix(1, 12)[0] + sind2[0]
                else:
                    for i in range(len(self.B12)):
                        sumSB2 = self.veiksmai.matrix_addition(sind2, [self.B12[i]])
                        if sum(sumSB2[0]) <= 2:
                            u = self.veiksmai.vectorE(i)[0] + sumSB2[0]
                    if u == []:
                        print("atsiuskite vektoriu is naujo")
        return u

# Dekodavimo funkcija, kuriai paduodamas 23-ų ilgio vektorius ir 
# grąžinamas 12-os ilgio dekoduotas vektorius.
# Pagal 3.7.1 skyriaus algoritmą.
    def dekoduoti(self, gautasVekt):
        # 1.
        nelyginisVekt = self.makeNelyginisVekt(gautasVekt)

        # 2.
        self.sindromas(nelyginisVekt)

        u = self.calcKlaidos()

        # v = w + u = nelyginisVekt + u
        v = self.veiksmai.matrix_addition(nelyginisVekt, [u])

        # 3. Pirmos 12 koordinačių yra dekoduotas vektorius. 
        result = v[0][:12]

        return result

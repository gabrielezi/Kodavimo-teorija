import numpy as np
import random
from veiksmai import Veiksmai
from duomenys import Duomenys

class Kodavimas:
    def __init__(self):
        duomenys = Duomenys()
        self.veiksmai = Veiksmai()
        self.G = duomenys.G

# Vektoriaus siuntimas kanalu ir iškraipymas. Kiekvienam siunčiamam vektoriaus elementui
# traukiamas atsitiktinis skaičius iš intervalo [0,1]. Jei a - mažesnis už nurodytą klaidos tikimybę-
# elementas bus iškraipytas, jei didesnis - ne.
# Funkcijai paduodamas 23-ų ilgio vektorius ir paklaida, grąžinamas iškraipytas 23-ų ilgio vektorius.
    def siustiKanalu(self, vekt, p):
        gaunamasVekt = self.veiksmai.zeros_matrix(1, len(vekt[0]))

        for i in range(len(vekt[0])):
            a = random.random()
            if a < p:
                gaunamasVekt[0][i] = (vekt[0][i]+1) % 2
            else:
                gaunamasVekt[0][i] = vekt[0][i]

        return gaunamasVekt

# Kodavimo funkcijai paduodamas 12-os ilgio vektorius ir grąžinamaa 23-ų ilgio 
# užkoduotas Golėjaus kodu vektorius. Atliekama daugyba pateikto vektoriaus ir G matricos.
    def uzkoduotiVektoriu(self, vekt):
        return self.veiksmai.matrix_multiply(vekt, self.G)
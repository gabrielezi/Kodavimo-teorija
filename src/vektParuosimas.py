import numpy as np
import random
    
class VektParuosimas:
# Skirtumų paieškos funkcija, kuriai paduodami originalus ir modifikuotas vektoriai,
# grąžinamas neatitikusių elementų vietų masyvas.
    def findDifferences(self, original, modified):
        differences = []
        for i in range(len(original[0])):
            if modified[0][i] != original[0][i]:
                differences.append(i)
        return differences

# Paduodamas tekstas paverčiamas binariniu kodu. Grąžinamos rašybos ženklų
# binarinės vertės atskirtos tarpais.
    def stringToBinary(self, text):
        res = ' '.join(format(ord(x), 'b') for x in text)
        return res

# Kiekvieno rašybos ženklo(binarine forma) vektoriaus gale pridedama 
# tiek nulių, kad vektorius būtų tinkamo ilgio(12).
# Funkcijai paduodamos rašybos ženklų binarinės vertės atskirtos tarpais,
# grąžinami sutvarkyti vektoriai ilgio 12 (pvz [110000100000, 110001000000]), bei pridėtų 0-ių kiekiai (pvz [5,5])
    def skaidytiBinary(self, text):
        skaidList = []
        addedZeros = []

        for binary_value in text:
                integer = binary_value
                for _ in range(12-len(binary_value)):
                    integer = integer + "0"
                addedZeros.append(12-len(binary_value))
                skaidList.append(int(integer))
        return skaidList, addedZeros

# Funkcijai paduodami sutvarkyti(ilgio 12) ir gauti išsiuntus kanalu binariniai vektoriai, bei pridėtų 0 kiekiai
# Funkcija binarius vektorius paverčia ascii simboliais ir grąžina tekstą.
    def binaryToString(self, binaryVektoriai, addedZeros):
        ascii_string = ""
        gautiVektoriai = []

        if len(binaryVektoriai[0]) == 23:
            for j in range(len(binaryVektoriai)):
                gautiVektoriai.append(binaryVektoriai[j][0:12])
        elif len(binaryVektoriai[0]) == 12:
            gautiVektoriai = binaryVektoriai

        for i in range(len(gautiVektoriai)):
            cutZeros = gautiVektoriai[i][0:len(gautiVektoriai[i])-addedZeros[i]]
            
            s = [str(i) for i in cutZeros] 
            joinedInt = int("".join(s), 2) 

            ascii_character = chr(joinedInt)
            ascii_string += ascii_character
        return ascii_string
    
# Funkcija paverčianti vektorius tinkamo formato, kad galimas būtų atvaizduoti paveikslėlis
# Suskirstoma eilutėmis ir stulpeliais pagal pradinio paveikslėlio parametrus
# Funkcijai paduodami gauti binariniai vektoriai, pridėtų 0 kiekiai, bei
# pradinio paveikslėlio stulpelių ir eilučių kiekiai
# Grąžinamas galutinis sutvarkytas sąrašas koordinačių.
    def formatBinaryForPicture(self, binaryVektoriai, addedZeros, len1, len2):
        gautiVektoriai = []
        intVekt = []

        if len(binaryVektoriai[0]) == 23:
            for j in range(len(binaryVektoriai)):
                gautiVektoriai.append(binaryVektoriai[j][0:12])
        elif len(binaryVektoriai[0]) == 12:
            gautiVektoriai = binaryVektoriai

        for i in range(len(gautiVektoriai)):
            cutZeros = gautiVektoriai[i][0:len(gautiVektoriai[i])-addedZeros[i]]
            
            s = [str(i) for i in cutZeros] 

            if s == 0 or s == []:
                joinedInt = 0
            else: joinedInt = int("".join(s), 2) 
            intVekt.append(joinedInt)

        k = 0
        row = []
        galutinisList = []

        for i in range(int(len(intVekt)/len2)):
            a = k * len2
            row = intVekt[a:a+len2]
            galutinisList.append(row)
            k += 1
        
        return galutinisList
import numpy as np
from tkinter import *
from tkinter import messagebox
from dekodavimas import Dekodavimas
from kodavimas import Kodavimas
from vektParuosimas import VektParuosimas

class WindowTekstas:
    @staticmethod
    def windowTekstas():
        def textEntered():
            enteredText = txt.get("1.0", END)

            #patikrinama, ar tikimybė korektiška
            try:
                if "," in txt2.get():
                    userP = float(txt2.get().replace(',','.'))
                else: userP = float(txt2.get())
            except ValueError:
                messagebox.showwarning('Neteisingi duomenys',
                                       'Klaidos tikimybė yra nekorektiška')

            skaidBinary, addedZeros = vektParuosimas.skaidytiBinary(vektParuosimas.stringToBinary(enteredText).split())

            nenaudojantKodo(skaidBinary, addedZeros, userP)
            naudojantKoda(skaidBinary, addedZeros, userP)

        def nenaudojantKodo(skaidBinary, addedZeros, p):
            lbl9.delete('1.0', END)

            gauti = []
            for vekt in skaidBinary:
                vektList = [int(d) for d in str(vekt)]
                gautasVekt = kodavimas.siustiKanalu([vektList], p)
                gauti.append(gautasVekt[0])
            
            lbl9.insert(INSERT, str(vektParuosimas.binaryToString(gauti, addedZeros)))
            
        def naudojantKoda( skaidBinary, addedZeros, p):
            lbl10.delete('1.0', END)
            uzkoduoti = []
            gauti = []
            dekoduoti = []
            for vekt in skaidBinary:
                vektList = [int(d) for d in str(vekt)]
                uzkoduotasVektorius = kodavimas.uzkoduotiVektoriu([vektList])
                uzkoduoti.append(uzkoduotasVektorius[0])

                gautasVekt = kodavimas.siustiKanalu(uzkoduotasVektorius, p)
                gauti.append(gautasVekt[0])
                dekoduotasVekt = dekodavimas.dekoduoti(gautasVekt)
                dekoduoti.append(dekoduotasVekt)

            lbl10.insert(INSERT, str(vektParuosimas.binaryToString(dekoduoti, addedZeros)))

        kodavimas = Kodavimas()
        vektParuosimas = VektParuosimas()
        dekodavimas = Dekodavimas(0, 0)
    

        newWindow = Toplevel()
        newWindow.geometry('820x600')

        lbl = Label(newWindow, text="Įveskite tekstą:")
        lbl.grid(column=0, row=0, pady=(5, 5)) 

        txt = Text(newWindow, width=35, height=5, font=("Arial", 12))
        txt.grid(column=0, row=1, pady=(5, 5))

        lbl1 = Label(newWindow, text="Įveskite klaidos tikimybę p:")
        lbl1.grid(column=0, row=2, pady=(5, 5))

        txt2 = Entry(newWindow, width=10, font=("Arial", 12))
        txt2.grid(column=0, row=3, pady=(5, 5))

        btn = Button(newWindow, text="Enter", bg="green",
                     fg="black", height=2, width=10, command=textEntered)

        btn.grid(column=0, row=4, pady=(5, 5))

        lbl6 = Label(newWindow, text="Dekoduotas tekstas:")
        lbl6.grid(column=0, row=5, pady=(5, 5))

        lbl7 = Label(newWindow, text="Nenaudojant kodo:")
        lbl7.grid(column=0, row=6, pady=(5, 5))

        lbl8 = Label(newWindow, text="Naudojant kodą:")
        lbl8.grid(column=1, row=6, pady=(5, 5))

        lbl9 = Text(newWindow,height=6, font=("Arial", "12"), width=40)
        lbl9.grid(padx=(20, 10),column=0, row=7, pady=(5, 5))

        lbl10 = Text(newWindow,height=6, font=("Arial", "12"), width=40)
        lbl10.grid(padx=(20, 10),column=1, row=7, pady=(5, 5))
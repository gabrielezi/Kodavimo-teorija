import numpy as np
from tkinter import *
from tkinter import messagebox
from dekodavimas import Dekodavimas
from kodavimas import Kodavimas
from vektParuosimas import VektParuosimas

class WindowVektorius:
    def __init__(self, uzkoduotasVekt, gautasVekt):
        self.uzkoduotasVekt = uzkoduotasVekt
        self.gautasVekt = gautasVekt

    def windowVektorius(self):
    # patikrinama ar tikrai įvestas binarinis vektorius ir ar tinkama tikimybė
        def checkIfBinary(vector, p):
            all_binary = all(c in '01' for c in vector)
            if all_binary and len(vector) == 12 and p >= 0.0 and p < 1.0:
                List = list(vector)
                List = [int(i) for i in List]
                return [List]
            else:
                messagebox.showwarning('Neteisingi duomenys',
                                    'Arba vektoriaus ilgis, arba klaidos tikimybė yra nekorektiški')

    # klaidingos koordinatės paryškinimas
        def highlight_char( lineno, start_char, end_char, bg_color=None, fg_color='red'):
            aText.tag_add(
                'tag1', f'{lineno}.{start_char}', f'{lineno}.{end_char}')
            aText.tag_config(
                'tag1', background=bg_color, foreground=fg_color)

        def vektoriusEntered():
            try:
                if "," in txt2.get():
                    userP = float(txt2.get().replace(',','.'))
                else: userP = float(txt2.get())
                userVector = checkIfBinary(txt.get(), userP)

            except ValueError:
                messagebox.showwarning('Neteisingi duomenys',
                                       'Arba vektoriaus ilgis, arba klaidos tikimybė yra nekorektiški')

            uzkoduotasVektorius = kodavimas.uzkoduotiVektoriu(userVector)
            self.uzkoduotasVekt = uzkoduotasVektorius
            a = str(uzkoduotasVektorius)

            lbl4.configure(text=a)

            gautasVekt = kodavimas.siustiKanalu(uzkoduotasVektorius, userP)
            self.gautasVekt = gautasVekt
            klaidos = vektParuosimas.findDifferences(
                uzkoduotasVektorius, gautasVekt)

            aText.delete('1.0', END)
            aText.insert(INSERT, str(gautasVekt))

            text = "Klaidu skaicius:  " + str(len(klaidos))
            lbl6.configure(text=text)

            for i in range(len(klaidos)):
                if klaidos[i] == 0:
                    highlight_char( lineno=1,
                                   start_char=klaidos[i]+2, end_char=klaidos[i]+3, fg_color='red')
                if klaidos[i] > 0:
                    highlight_char( lineno=1,
                                   start_char=klaidos[i]*3 + 2, end_char=klaidos[i]*3+3, fg_color='red')

        def updateVector():
            getText = list(list(aText.get("1.0", END)))
            item_list = [e for e in getText if e not in (
                '[', ']', '\n', ' ', ',')]
            convertText = [int(i) for i in item_list]
            self.gautasVekt = [convertText]
            lbl8.configure(text="Redaguota")
            klaidos = vektParuosimas.findDifferences(
                self.uzkoduotasVekt, [convertText])
            text = "Klaidu skaicius:  " + str(len(klaidos))
            lbl6.configure(text=text)

        def dekoduotiEntered():
            dekoduotasVekt = dekodavimas.dekoduoti(self.gautasVekt)
            lbl10.configure(text=str(dekoduotasVekt))

        kodavimas = Kodavimas()
        vektParuosimas = VektParuosimas()
        dekodavimas = Dekodavimas( 0, 0)

        newWindow = Toplevel()
        newWindow.geometry('820x500')

        lbl = Label(newWindow, text="Įveskite vektorių (ilgio 12):")
        lbl.grid(column=0, row=0, pady=(5, 5)) 

        txt = Entry(newWindow, width=20, font=("Arial", 12))
        txt.grid(column=0, row=1, pady=(5, 5))

        lbl2 = Label(newWindow, text="Įveskite klaidos tikimybę p:")
        lbl2.grid(column=0, row=2, pady=(5, 5))

        txt2 = Entry(newWindow, width=10, font=("Arial", 12))
        txt2.grid(column=0, row=3, pady=(5, 5))

        btn = Button(newWindow, text="Enter", bg="yellow",
                     fg="black", height=2, width=10, command=vektoriusEntered)

        btn.grid(column=1, row=3, pady=(5, 5))

        lbl3 = Label(
            newWindow, text="Vektorius, užkoduotas kodu C23:", fg="blue")
        lbl3.grid(column=0, row=4, pady=(5, 5))
        lbl4 = Label(newWindow, text="", width=50, font=("Arial", 12))
        lbl4.grid(column=0, row=5, pady=(5, 5))

        lbl5 = Label(
            newWindow, text="Vektorius, gautas išsiuntus kanalu:", fg="blue")
        lbl5.grid(column=0, row=6, pady=(5, 5))

        aText = Text(newWindow, height=2, font=("Arial", "12"), width=45)
        aText.grid(padx=(20, 10), column=0, row=7, pady=(5, 5))
        lbl6 = Label(
            newWindow, text="Klaidų skaičius:", fg="blue")
        lbl6.grid(column=1, row=5, pady=(5, 5))

        btn2 = Button(newWindow, text="Redaguoti iš kanalo išėjusį vektorių", bg="yellow",
                      fg="black", width=30, height=2, command=updateVector)

        btn2.grid(column=1, row=7, pady=(5, 5))
        lbl8 = Label(newWindow, text="", fg="blue")
        lbl8.grid(column=2, row=7, pady=(5, 5))

        btn3 = Button(newWindow, text="Dekoduoti", bg="orange",
                      fg="black", width=30, height=2, command=dekoduotiEntered)

        btn3.grid(column=0, row=8, pady=(5, 5))
        lbl9 = Label(
            newWindow, text="Dekoduotas vektorius:", fg="blue")
        lbl9.grid(column=0, row=9, pady=(5, 5))
        lbl10 = Label(newWindow, text="", font=("Arial", 12))
        lbl10.grid(column=0, row=10, pady=(5, 5))
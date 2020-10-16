import numpy as np
from tkinter import *
from tkinter import messagebox
from veiksmai import Veiksmai
from dekodavimas import Dekodavimas


class Duomenys:
    def __init__(self):
        veiksmai = Veiksmai()
        self.I = veiksmai.identity_matrix(12)
        self.B = [
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

        self.B12 = [
            [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
            [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
            [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],  # 11
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

        G = veiksmai.zeros_matrix(12, 23)
        for j in range(len(self.I)):
            row = self.I[j] + self.B[j]
            G[j] = row
        self.G = G


class Vektoriai:
    def __init__(self, uzkoduotasVekt, gautasVekt):
        self.uzkoduotasVekt = uzkoduotasVekt
        self.gautasVekt = gautasVekt


if __name__ == '__main__':
    vektoriai = Vektoriai([], [])

    def checkIfBinary(vector, p):
        all_binary = all(c in '01' for c in vector)
        if all_binary and len(vector) == 12 and p >= 0.0 and p < 1.0:
            List = list(vector)
            List = [int(i) for i in List]
            return [List]
        else:
            messagebox.showwarning('Neteisingi duomenys',
                                   'Arba vektoriaus ilgis, arba klaidos tikimybė yra nekorektiški')

    def windowVektorius():
        def highlight_char(tag_name, lineno, start_char, end_char, bg_color=None, fg_color=None):
            aText.tag_add(
                tag_name, f'{lineno}.{start_char}', f'{lineno}.{end_char}')
            aText.tag_config(
                tag_name, background=bg_color, foreground=fg_color)

        def vektoriusEntered():
            try:
                userP = float(txt2.get())
                userVector = checkIfBinary(txt.get(), userP)

            except ValueError:
                messagebox.showwarning('Neteisingi duomenys',
                                       'Arba vektoriaus ilgis, arba klaidos tikimybė yra nekorektiški')

            uzkoduotasVektorius = veiksmai.uzkoduotiVektoriu(
                userVector, duomenys.G)
            vektoriai.uzkoduotasVekt = uzkoduotasVektorius
            a = str(uzkoduotasVektorius)

            lbl4.configure(text=a)

            gautasVekt = veiksmai.siustiKanalu(uzkoduotasVektorius, p)
            vektoriai.gautasVekt = gautasVekt
            klaidos = veiksmai.findDifferences(
                uzkoduotasVektorius, gautasVekt)

            aText.insert(INSERT, str(gautasVekt))

            text = "Klaidu skaicius:  " + str(len(klaidos))
            lbl6.configure(text=text)

            for i in range(len(klaidos)):
                if klaidos[i] == 0:
                    highlight_char(tag_name='tag1', lineno=1,
                                   start_char=klaidos[i]+2, end_char=klaidos[i]+3, fg_color='red')
                if klaidos[i] > 0:
                    highlight_char(tag_name='tag1', lineno=1,
                                   start_char=klaidos[i]*3 + 2, end_char=klaidos[i]*3+3, fg_color='red')

        def updateVector():
            getText = list(list(aText.get("1.0", END)))
            item_list = [e for e in getText if e not in (
                '[', ']', '\n', ' ', ',')]
            convertText = [int(i) for i in item_list]
            vektoriai.gautasVekt = [convertText]
            lbl8.configure(text="Redaguota")
            klaidos = veiksmai.findDifferences(
                vektoriai.uzkoduotasVekt, [convertText])
            text = "Klaidu skaicius:  " + str(len(klaidos))
            lbl6.configure(text=text)

        def dekoduotiEntered():
            print(vektoriai.gautasVekt)
            dekoduotasVekt = dekodavimas.dekoduoti(
                vektoriai.gautasVekt, duomenys.B12)
            lbl10.configure(text=str(dekoduotasVekt))

        newWindow = Toplevel(window)
        newWindow.geometry('820x400')

        lbl = Label(newWindow, text="Iveskite vektoriu:")
        lbl.grid(column=0, row=0, pady=(5, 5))  # sticky="W"

        txt = Entry(newWindow, width=20, font=("Arial", 12))
        txt.grid(column=0, row=1, pady=(5, 5))

        lbl2 = Label(newWindow, text="Iveskite klaidos tikimybe p:")
        lbl2.grid(column=0, row=2, pady=(5, 5))

        txt2 = Entry(newWindow, width=10, font=("Arial", 12))
        txt2.grid(column=0, row=3, pady=(5, 5))

        btn = Button(newWindow, text="Enter", bg="yellow",
                     fg="black", height=2, width=10, command=vektoriusEntered)

        btn.grid(column=1, row=3, pady=(5, 5))

        lbl3 = Label(
            newWindow, text="Vektorius, uzkoduotas kodu C23:", fg="blue")
        lbl3.grid(column=0, row=4, pady=(5, 5))
        lbl4 = Label(newWindow, text="", width=50, font=("Arial", 12))
        lbl4.grid(column=0, row=5, pady=(5, 5))

        lbl5 = Label(
            newWindow, text="Vektorius, gautas issiuntus kanalu:", fg="blue")
        lbl5.grid(column=0, row=6, pady=(5, 5))

        aText = Text(newWindow, height=2, font=("Arial", "12"), width=45)
        aText.grid(padx=(20, 10), column=0, row=7, pady=(5, 5))
        lbl6 = Label(
            newWindow, text="Klaidu skaicius:", fg="blue")
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

    def windowTekstas():
        def stringToBinary():
            enteredText = txt.get("1.0", END)
            print(enteredText)
            print(veiksmai.stringToBinary(enteredText))
            skaidBinary, addedZeros = veiksmai.skaidytiBinary(veiksmai.stringToBinary(enteredText))
            uzkoduotasVektorius = veiksmai.uzkoduotiVektoriu(
                userVector, duomenys.G)

        newWindow = Toplevel(window)
        newWindow.geometry('820x400')

        lbl = Label(newWindow, text="Iveskite tekstą:")
        lbl.grid(column=0, row=0, pady=(5, 5)) 

        txt = Text(newWindow, width=35, height=5, font=("Arial", 12))
        txt.grid(column=0, row=1, pady=(5, 5))

        btn = Button(newWindow, text="Enter", bg="green",
                     fg="black", height=2, width=10, command=stringToBinary)

        btn.grid(column=1, row=1, pady=(5, 5))

    def windowPaveikslelis():
        newWindow = Toplevel(window)

    p = 0.1000

    duomenys = Duomenys()
    veiksmai = Veiksmai()
    dekodavimas = Dekodavimas(0, 0, 0)

    H = duomenys.I + duomenys.B12
    dekodavimas.H = H

#---------------------------------------------------------------------------- Kodavimas

    # user_input = [[0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1]]  # 12

    # uzkoduotasVektorius = veiksmai.uzkoduotiVektoriu(user_input, duomenys.G)
    # print('uzkoduotas kodas: ', uzkoduotasVektorius)

    # gautasVekt = veiksmai.siustiKanalu(uzkoduotasVektorius, p)
    # print('gautas kodas    : ', gautasVekt)

    # dekodavimas.dekoduoti(gautasVekt, duomenys.B12)
# ---------------------------------------------------------------------------------
    window = Tk()
    window.title("Golejaus Kodas")
    window.geometry('450x180')

    lbl = Label(window, text="Pasirinkite scenariju:")
    lbl.grid(column=0, row=0)

    btn = Button(window, text="Vektorius", bg="yellow",
                 fg="black", command=windowVektorius,  height=5, width=20)

    btn.grid(column=0, row=2)

    btn2 = Button(window, text="Tekstas", bg="orange",
                  fg="black", command=windowTekstas, height=5, width=20)

    btn2.grid(column=1, row=2)

    btn3 = Button(window, text="Paveikslelis", bg="brown",
                  fg="white", command=windowPaveikslelis,  height=5, width=20)

    btn3.grid(column=2, row=2)

    window.mainloop()

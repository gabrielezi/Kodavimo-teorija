import numpy as np
from numpy import asarray 
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
from dekodavimas import Dekodavimas
from windowVektorius import WindowVektorius
from windowTekstas import WindowTekstas
from kodavimas import Kodavimas
from vektParuosimas import VektParuosimas

class WindowPaveikslelis:
    def __init__(self, uzkoduotiVekt, gautiVekt):  
        self.uzkoduotiVekt = uzkoduotiVekt
        self.gautiVekt = gautiVekt

    def windowPaveikslelis(self): 
        def browse_button():
            filename = filedialog.askopenfile().name

            load = Image.open(filename).convert('L')
            render = ImageTk.PhotoImage(load)
            img = Label(newWindow, image=render)
            img.image = render
            img.grid(row=1, column=0)

            data = asarray(load) 
            self.gautiVekt = data 
    
        def pictureEntered():
            try:
                if "," in txt2.get():
                    userP = float(txt2.get().replace(',','.'))
                else: userP = float(txt2.get())
            except ValueError:
                messagebox.showwarning('Neteisingi duomenys',
                                       'Klaidos tikimybė yra nekorektiška')

            pictureArrayBinary = []
            arrayBinary = []
            
            for i in range(len(self.gautiVekt)):
                row = []
                for j in range(len(self.gautiVekt[i])):
                    a = bin(self.gautiVekt[i][j])[2:]
                    row.append(a)
                    arrayBinary.append(a)
                pictureArrayBinary.append(row)

            len1 = len(pictureArrayBinary)
            len2 = len(pictureArrayBinary[0])

            skaidBinary, addedZeros = vektParuosimas.skaidytiBinary(arrayBinary)

            nenaudojantKodo(skaidBinary, addedZeros, userP, len1, len2)
            naudojantKoda(skaidBinary, addedZeros, userP, len1, len2)


        def nenaudojantKodo(skaidBinary, addedZeros, p, len1, len2):
            gauti = []
            for vekt in skaidBinary:
                vektList = [int(d) for d in str(vekt)]
                gautasVekt = kodavimas.siustiKanalu([vektList], p)
                gauti.append(gautasVekt[0])

            array = np.array(vektParuosimas.formatBinaryForPicture(gauti, addedZeros, len1, len2), dtype=np.uint8)
            pilImage = Image.fromarray(array)
            render2 = ImageTk.PhotoImage(pilImage)
            img2 = Label(newWindow, image=render2)
            img2.image = render2
            img2.grid(row=6, column=0)
            
        def naudojantKoda( skaidBinary, addedZeros, p, len1, len2):
            uzkoduoti = []
            gauti = []
            dekoduoti = []
            for vekt in skaidBinary:
                vektList = [int(d) for d in str(vekt)]
                if vekt == 0:
                    vektList.extend([0,0,0,0,0,0,0,0,0,0,0])
                uzkoduotasVektorius = kodavimas.uzkoduotiVektoriu([vektList])
                uzkoduoti.append(uzkoduotasVektorius[0])

                gautasVekt = kodavimas.siustiKanalu(uzkoduotasVektorius, p)
                gauti.append(gautasVekt[0])
                dekoduotasVekt = dekodavimas.dekoduoti(gautasVekt)
                dekoduoti.append(dekoduotasVekt)

            array = np.array(vektParuosimas.formatBinaryForPicture(dekoduoti, addedZeros, len1, len2), dtype=np.uint8)
            pilImage = Image.fromarray(array)
            render2 = ImageTk.PhotoImage(pilImage)
            img2 = Label(newWindow, image=render2)
            img2.image = render2
            img2.grid(row=6, column=1)

        kodavimas = Kodavimas()
        vektParuosimas = VektParuosimas()
        dekodavimas = Dekodavimas(0, 0)

                
        newWindow = Toplevel()
        newWindow.geometry('700x600')

        button2 = Button(newWindow,text="Pasirinkite paveikslėlį", command=browse_button)
        button2.grid(row=0, column=0, pady=(5, 5))

        lbl1 = Label(newWindow, text="Įveskite klaidos tikimybę p:")
        lbl1.grid(column=0, row=2, pady=(5, 5))

        txt2 = Entry(newWindow, width=10, font=("Arial", 12))
        txt2.grid(column=0, row=3, pady=(5, 5))

        btn = Button(newWindow, text="Enter", bg="green",
                        fg="black", height=2, width=10, command=pictureEntered)

        btn.grid(column=0, row=4, pady=(5, 5))

        lbl2 = Label(newWindow, text="Nenaudojant kodo:")
        lbl2.grid(column=0, row=5, pady=(5, 5))

        lbl3 = Label(newWindow, text="Naudojant kodą:")
        lbl3.grid(column=1, row=5, pady=(5, 5))

        lbl4 = Label(newWindow, text="")
        lbl4.grid(column=1, row=1, pady=(5, 5), width=30)
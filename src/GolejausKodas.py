import numpy as np
from numpy import asarray 
from tkinter import *
from windowVektorius import WindowVektorius
from windowTekstas import WindowTekstas
from windowPaveikslelis import WindowPaveikslelis

from kodavimas import Kodavimas
from dekodavimas import Dekodavimas


if __name__ == '__main__':
    windowVektorius = WindowVektorius([], [])
    windowPaveikslelis = WindowPaveikslelis([], [])

    window = Tk()
    window.title("Golėjaus Kodas")
    window.geometry('450x180')

    lbl = Label(window, text="Pasirinkite scenarijų:")
    lbl.grid(column=0, row=0)

    btn = Button(window, text="Vektorius", bg="yellow",
                 fg="black", command=windowVektorius.windowVektorius,  height=5, width=20)

    btn.grid(column=0, row=2)

    btn2 = Button(window, text="Tekstas", bg="orange",
                  fg="black", command=WindowTekstas.windowTekstas, height=5, width=20)

    btn2.grid(column=1, row=2)

    btn3 = Button(window, text="Paveikslėlis", bg="brown",
                  fg="white", command=windowPaveikslelis.windowPaveikslelis,  height=5, width=20)

    btn3.grid(column=2, row=2)

    window.mainloop()

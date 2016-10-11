from tkinter import *
from random import randint

class TicTac:
    def __init__(self):
        window = Tk()
        window.title("Display Tic Tac")

        x = PhotoImage(file = "image/x.gif")
        o = PhotoImage(file = "image/o.gif")
        
        for i in range(9):
            if randint(0,1):
                Label(window, image = x).grid(row = i // 3, column = i % 3)
            else:
                Label(window, image = o).grid(row = i // 3, column = i % 3)

        window.mainloop()

TicTac()

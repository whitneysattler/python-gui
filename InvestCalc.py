from tkinter import *
from math import *

class InvestmentCalc:
    def __init__(self):
        window = Tk()
        window.title("Investment Calculator")

        frame0 = Frame(window)
        frame0.pack()

        Label(frame0, text = "Investment Amount:").grid(row = 1, column = 1, sticky = W)
        self.v1 = StringVar()
        Entry(frame0, textvariable = self.v1, justify = RIGHT).grid(row = 1, column = 2, padx = 5, pady = 2)
        Label(frame0, text = "Years:").grid(row = 2, column = 1, sticky = W)
        self.v2 = StringVar()
        Entry(frame0, textvariable = self.v2, justify = RIGHT).grid(row = 2, column = 2, padx = 5, pady = 2)
        Label(frame0, text = "Annual Interest Rate:").grid(row = 3, column = 1, sticky = W)
        self.v3 = StringVar()
        Entry(frame0, textvariable = self.v3, justify = RIGHT).grid(row = 3, column = 2, padx = 5, pady = 2)
        Label(frame0, text = "Future Value:").grid(row = 4, column = 1, sticky = W)
        self.v4 = StringVar()
        Label(frame0, textvariable = self.v4).grid(row = 4, column = 2, sticky = E)
        Button(frame0, command = self.calc, text = "Calculate").grid(row = 5, column = 2, sticky = E)

        window.mainloop()

    def calc(self):
        self.v4.set(format(float(self.v1.get()) * (1 + float(self.v3.get())/1200)**(float(self.v2.get())*12), "10.2f"))

InvestmentCalc()

        

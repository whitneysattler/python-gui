from tkinter import *

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")

        Label(window, text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5, column = 1, sticky = W)

        self.AnnualInterestRate = StringVar()
        Entry(window, textvariable = self.AnnualInterestRate, justify = RIGHT).grid(row = 1, column = 2, padx = 5, pady = 5)
        self.numberOfYears = StringVar()
        Entry(window, textvariable = self.numberOfYears, justify = RIGHT).grid(row = 2, column = 2, padx = 5, pady = 5)
        self.loanAmount = StringVar()
        Entry(window, textvariable = self.loanAmount, justify = RIGHT).grid(row = 3, column = 2, padx = 5, pady = 5)
        self.monthlyPayment = StringVar()
        Label(window, textvariable = self.monthlyPayment).grid(row = 4, column = 2, sticky = E, padx = 5, pady = 5)
        self.totalPayment = StringVar()
        Label(window, textvariable = self.totalPayment).grid(row = 5, column = 2, sticky = E, padx = 5, pady = 5)
        Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 6, column = 2, sticky = E, padx = 5, pady = 5)

        window.mainloop() # Create an event loop

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(float(self.loanAmount.get()), float(self.AnnualInterestRate.get()) / 1200, int(self.numberOfYears.get()))
        self.monthlyPayment.set(format(monthlyPayment, "10.2f"))
        totalPayment = float(self.monthlyPayment.get()) * 12 * int(self.numberOfYears.get())
        self.totalPayment.set(format(totalPayment, "10.2f"))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

LoanCalculator() # Create GUI
                                                

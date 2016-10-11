from tkinter import *

class LoanCompare:
    def __init__(self):
        window = Tk()
        window.title("Loan Compare")

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text = "Loan Amount").pack(side = LEFT)
        self.amount = StringVar()
        Entry(frame1, textvariable = self.amount, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text = "Years").pack(side = LEFT)
        self.years = StringVar()
        Entry(frame1, textvariable = self.years, justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Calculate", command = self.processButton).pack(side = LEFT)

        self.text = Text(window) # Create and add text to the window
        self.text.pack()
        self.text.insert(END, format("Interest Rate", "30s") + format("Monthly Payment", "30s") + "Total Payment\n")
            
        self.text.mark_set("table", INSERT)
        self.text.mark_gravity("table", LEFT)

        window.mainloop()

    def processButton(self):
        self.text.delete("table", END)
        self.text.insert("table", "\n")
        
        for i in range(0, 25):
            monthlyPayment = self.getMonthlyPayment(float(self.amount.get()), (.05 + i * 0.0125)/12, int(self.years.get()))
            totalPayment = monthlyPayment * 12 * int(self.years.get())
            self.text.insert(END, format(5 + i * 0.125, "<30.2f"))
            self.text.insert(END, "$" + format(monthlyPayment, "<29.2f"))
            self.text.insert(END, "$" +format(totalPayment, "<.2f") + "\n")
            
        return

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))        
        return monthlyPayment

LoanCompare()
        

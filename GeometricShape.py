from tkinter import *

class GeometricButtons:
    def __init__(self):
        window = Tk()
        window.title("Radiobuttons and Checkbuttons")

        self.canvas = Canvas(window, bg = "white", width = 200, height = 50)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()
        self.v1 = StringVar()
        btRect = Radiobutton(frame1, text = "Rectangle", variable = self.v1, value = "r", command = self.processButton)
        btOval = Radiobutton(frame1, text = "Oval", variable = self.v1, value = "o", command = self.processButton)
        self.v2 = IntVar()
        cbtFilled = Checkbutton(frame1, text = "Filled", variable = self.v2, command = self.processButton)

        btRect.grid(row = 1, column = 1)
        btOval.grid(row = 1, column = 2)
        cbtFilled.grid(row = 1, column = 3)

        window.mainloop()

    def processButton(self):
        self.canvas.delete("rect", "oval")
        if (self.v1.get() == "r"):
            if (self.v2.get() == 1):
                self.canvas.create_rectangle(10, 10, 190, 40, tags = "rect", fill = "red")
            else:
                self.canvas.create_rectangle(10, 10, 190, 40, tags = "rect")
        else:
            if (self.v2.get() == 1):
                self.canvas.create_oval(10, 10, 190, 40, tags = "oval", fill = "red")
            else:
                self.canvas.create_oval(10, 10, 190, 40, tags = "oval")
    
GeometricButtons()

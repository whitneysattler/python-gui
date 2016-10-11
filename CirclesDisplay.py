from tkinter import *

class CircleAdder:
    def __init__(self):
        window = Tk()
        window.title("Display Circles")
        self.centerX = 250
        self.centerY = 250
        self.canvas = Canvas(window, width = self.centerX * 2, height = self.centerY * 2, bg = "white")
        self.canvas.pack()

        self.radius = 25

        self.canvas.create_oval(self.centerX - self.radius, self.centerY - self.radius, self.centerX + self.radius, self.centerY + self.radius, tags = "circle" + str(self.radius))

        self.canvas.bind("<Button-1>", self.addCircle)
        self.canvas.bind("<Button-3>", self.delCircle)

        window.mainloop()

    def addCircle(self, event):
        self.radius += 5
        self.canvas.create_oval(self.centerX - self.radius, self.centerY - self.radius, self.centerX + self.radius, self.centerY + self.radius, tags = "circle" + str(self.radius))

    def delCircle(self, event):
        self.canvas.delete("circle" + str(self.radius))
        if self.radius >= 30:
            self.radius -= 5

CircleAdder()

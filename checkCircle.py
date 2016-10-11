from tkinter import *
from math import *

class inRect:
    def __init__(self, xCord, yCord, rad):
        self.xCord = xCord
        self.yCord = yCord
        self.radius = rad

        window = Tk()
        window.title("Inside the Circle?")

        self.canvas = Canvas(window, width = 300, height = 250, bg = "white")
        self.canvas.pack()

        self.canvas.create_oval(self.xCord - self.radius, self.yCord - self.radius, \
                                self.xCord + self.radius, self.yCord + self.radius)

        self.canvas.bind("<B1-Motion>", self.checkIn)
        self.canvas.bind("<ButtonRelease-1>", self.delete)

        window.mainloop()

    def checkIn(self, event):
        self.canvas.delete("inText")
        if self.inCircle(event.x, event.y):
            insert = ""
        else:
            insert = "not "
        self.canvas.create_text(event.x, event.y, text = "Mouse pointer is " + insert + "in circle", tags = "inText")
        
    def delete(self, event):
        self.canvas.delete("inText")
        
    def inCircle(self, x, y):
        distance = sqrt((self.xCord - x) * (self.xCord - x) + (self.yCord - y) * (self.yCord - y))
        return distance <= self.radius

inRect(100, 60, 50)

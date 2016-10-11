from tkinter import *
from Rectangle2D import Rectangle2D

class inRect:
    def __init__(self, xCord, yCord, width, height):
        self.xCord = xCord
        self.yCord = yCord
        self.width = width
        self.height = height

        window = Tk()
        window.title("Inside the Rectangle?")

        self.canvas = Canvas(window, width = 300, height = 250, bg = "white")
        self.canvas.pack()

        self.canvas.create_rectangle(xCord - (width/2), yCord - (height/2), \
                                     xCord + (width/2), yCord + (height/2))

        self.canvas.bind("<B1-Motion>", self.checkIn)
        self.canvas.bind("<ButtonRelease-1>", self.delete)

        window.mainloop()

    def checkIn(self, event):
        self.canvas.delete("inText")
        rect = Rectangle2D(self.xCord, self.yCord, self.width, self.height)
        if rect.containsPoint(event.x, event.y):
            insert = ""
        else:
            insert = "not "
        self.canvas.create_text(event.x, event.y, text = "Mouse pointer is " + insert + "in rectangle", tags = "inText")
        
    def delete(self, event):
        self.canvas.delete("inText")

inRect(100, 60, 100, 40)

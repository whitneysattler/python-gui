from tkinter import * # import all definitions from tkinter
from math import *

class EnlargeShrinkCircle:
    def __init__(self):
        self.radius = 50

        window = Tk()
        window.title("Control Circle Demo") # Set a title

        self.canvas = Canvas(window, bg = "white", height = 200, width = 200)
        self.canvas.pack()
        self.canvas.create_oval(100 - self.radius, 100 - self.radius, 100 + self.radius, 100 + self.radius, tags = "oval")

        # Bind canvas to slide event
        self.canvas.bind("<B1-Motion>", self.changeCircle)

        window.mainloop() # Create an event loop

    def changeCircle(self, event):
        self.canvas.delete("oval")
        self.radius = self.distance(event.x, event.y)
        self.canvas.create_oval(100 - self.radius, 100 - self.radius, 100 + self.radius, 100 + self.radius, tags = "oval")

    def distance(self, x, y):
        xDist = 100 - x
        yDist = 100 - y
        return sqrt(xDist*xDist + yDist*yDist)


EnlargeShrinkCircle() # Create GUI

from tkinter import *
from Point import Point

class TwoCircles:
    def __init__(self):
        window = Tk()
        window.title("Two Circles")

        self.canvas = Canvas(window, width = 500, height =300, bg = "white")
        self.canvas.pack()

        self.p1 = Point(175, 150)
        self.p2 = Point(325, 150)
        self.points = [self.p1, self.p2]

        self.canvas.create_oval
        window.mainloop()

TwoCircles()

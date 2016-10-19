from tkinter import *
from Point import *
from math import *
from random import randint

class ArrowCreator:
    def __init__(self):
        window = Tk()
        window.title("Create Arrow")

        self.canvas = Canvas(window, width = 500, height = 300, bg = "white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.clickArrow)
        self.canvas.bind("<B1-Motion>", self.dragArrow)

        Button(window, text = "Create Arrow", command = self.generateArrow).pack()
        self.origin = Point(0,0)
        window.mainloop()


    def clickArrow(self, event):
        self.canvas.delete("arrow")
        self.origin.setX(event.x)
        self.origin.setY(event.y)

    def dragArrow(self, event):
        self.canvas.delete("arrow")
        self.drawArrow(event.x, event.y)

    def drawArrow(self, x, y):
        self.canvas.create_line(self.origin.getX(), self.origin.getY(), x,y, tags = "arrow")
        mag = self.origin.distance(Point(x, y))
        origVector = [x - self.origin.getX(), y - self.origin.getY()]
        negativeVector = [-i for i in origVector]
        scaledVector = [i * 10 / mag for i in negativeVector]
        centerX = x + scaledVector[0]
        centerY = y + scaledVector[1]
        changeVector = [scaledVector[0] * 0.5 - scaledVector[1] * sqrt(3)/2, scaledVector[0] * sqrt(3)/2 + scaledVector[1] * 0.5]
        self.canvas.create_polygon(x, y, x + negativeVector[0]*10/mag, y + negativeVector[1]*10/mag, centerX + changeVector[0], centerY + changeVector[1], tags = "arrow")
        changeVector = [scaledVector[0] * 0.5 + scaledVector[1] * sqrt(3)/2, -scaledVector[0] * sqrt(3)/2 + scaledVector[1] * 0.5]       
        self.canvas.create_polygon(x, y, x + negativeVector[0]*10/mag, y + negativeVector[1]*10/mag, centerX + changeVector[0], centerY + changeVector[1], tags = "arrow")

    def generateArrow(self):
        self.canvas.delete("arrow")
        self.origin.setX(randint(0, 500))
        self.origin.setY(randint(0, 300))
        destX = randint(-1 * self.origin.getX(), 500 - self.origin.getX())
        destY = randint(-1 * self.origin.getY(), 300 - self.origin.getY())
        self.drawArrow(self.origin.getX() + destX, self.origin.getY() + destY)
        

ArrowCreator()
        

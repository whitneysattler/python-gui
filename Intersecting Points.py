from tkinter import *
from Point import Point

class IntersectingPoints:
    def __init__(self, p1X = 20, p1Y = 20, p2X = 56, p2Y = 130, p3X = 100, p3Y = 20, p4X = 16, p4Y = 130):
        window = Tk()
        window.title("Intersecting Points")

        self.p1 = Point(p1X, p1Y)
        self.p2 = Point(p2X, p2Y)
        self.p3 = Point(p3X, p3Y)
        self.p4 = Point(p4X, p4Y)
        self.points = [self.p1, self.p2, self.p3, self.p4]
        self.activePoint = self.p1
        self.draggable = False

        self.canvas = Canvas(window, width = 300, height = 250, bg = "white")
        self.canvas.pack()
        self.canvas.create_line(self.p1.getX(), self.p1.getY(), self.p2.getX(), self.p2.getY(), tag = "line")
        self.canvas.create_line(self.p3.getX(), self.p3.getY(), self.p4.getX(), self.p4.getY(), tag = "line")

        self.calcIntersect()

        self.canvas.bind("<Button-1>", self.processClick)
        self.canvas.bind("<B1-Motion>", self.processDrag)
        self.canvas.bind("<ButtonRelease-1>", self.processUp)
        
    def calcIntersect(self):
        e = (self.p1.getY() - self.p2.getY()) * self.p1.getX() - (self.p1.getX() - self.p2.getX()) * self.p1.getY()
        f = (self.p3.getY() - self.p4.getY()) * self.p3.getX() - (self.p3.getX() - self.p4.getX()) * self.p3.getY()
        a = self.p1.getY() - self.p2.getY()
        b = -(self.p1.getX() - self.p2.getX())
        c = self.p3.getY() - self.p4.getY()
        d = -(self.p3.getX() - self.p4.getX())
        if ((a * d - b * c) == 0):
            return
        x = ((e * d) - (b * f)) / ((a * d) - (b * c))
        y = ((a * f) - (e * c)) / ((a * d) - (b * c))
        if x >= min(self.p1.getX(), self.p2.getX()) and x >= min(self.p3.getX(), self.p4.getX()) and x <= max(self.p1.getX(), self.p2.getX()) and x <= max(self.p3.getX(), self.p4.getX()):
            if y >= min(self.p1.getY(), self.p2.getY()) and y >= min(self.p3.getY(), self.p4.getY()) and y <= max(self.p1.getY(), self.p2.getY()) and  y <= max(self.p3.getY(), self.p4.getY()):
                self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill = "black", tag = "intercept")
                self.canvas.create_text(x, y - 8, text = "(" + str(round(x,0)) + "," + str(round(y,0)) + ")", tag = "intercept")

    def processClick(self, event):
        mousePoint = Point(event.x, event.y)
        closestPoint = self.p1
        for point in self.points:
            if mousePoint.distance(point) <= mousePoint.distance(closestPoint):
                closestPoint = point
        if mousePoint.isNearBy(closestPoint):
            self.activePoint = closestPoint
            self.draggable = True

    def processDrag(self, event):
        if self.draggable:
            self.canvas.delete("line", "intercept")
            self.activePoint.setX(event.x)
            self.activePoint.setY(event.y)
            self.canvas.create_line(self.p1.getX(), self.p1.getY(), self.p2.getX(), self.p2.getY(), tag = "line")
            self.canvas.create_line(self.p3.getX(), self.p3.getY(), self.p4.getX(), self.p4.getY(), tag = "line")
            self.calcIntersect()

    def processUp(self, event):
        self.draggable = False
IntersectingPoints()

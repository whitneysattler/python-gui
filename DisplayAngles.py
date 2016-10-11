from tkinter import *
from Point import Point
import math

class TriAngles:
    def __init__(self):
        window = Tk()
        window.title("Triangle Angles")

        self.canvas = Canvas(window, width = 300, height = 200, bg = "white")
        self.canvas.pack()
        self.p1 = Point(40, 40)
        self.p2 = Point(80, 80)
        self.p3 = Point(40, 80)
        self.points = [self.p1, self.p2, self.p3]
        self.activePoint = self.p1
        self.draggable = False
        self.drawTriangle()
        self.drawAngles()

        self.canvas.bind("<Button-1>", self.processClick)
        self.canvas.bind("<B1-Motion>", self.processDrag)
        self.canvas.bind("<ButtonRelease-1>", self.processUp)

        window.mainloop()

    def drawTriangle(self):
        self.canvas.create_polygon(self.p1.getX(), self.p1.getY(), self.p2.getX(), self.p2.getY(), self.p3.getX(), self.p3.getY(), fill = "yellow", tag = "triangle")

    def processClick(self, event):
        self.canvas.delete("angles")
        mousePoint = Point(event.x, event.y)
        closestPoint = self.p1
        for point in self.points:
            if mousePoint.distance(point) <= mousePoint.distance(closestPoint):
                closestPoint = point
        if mousePoint.isNearBy(closestPoint):
            self.activePoint = closestPoint
            self.draggable = True

    def processDrag(self, event):
        if self.draggable == True:
            self.canvas.delete("triangle")
            self.activePoint.setX(event.x)
            self.activePoint.setY(event.y)
            self.canvas.create_polygon(self.p1.getX(), self.p1.getY(), self.p2.getX(), self.p2.getY(), self.p3.getX(), self.p3.getY(), fill = "yellow", tag = "triangle")

    def processUp(self, event):
        self.drawAngles()
        self.draggable = False

    def drawAngles(self):
        dist1 = self.p2.distance(self.p3)
        dist2 = self.p3.distance(self.p1)
        dist3 = self.p1.distance(self.p2)
        angle1 = math.degrees(math.acos((dist1 * dist1 - dist2 * dist2 - dist3 * dist3) / (-2 * dist2 * dist3)))
        angle2 = math.degrees(math.acos((dist2 * dist2 - dist1 * dist1 - dist3 * dist3) / (-2 * dist1 * dist3)))
        angle3 = math.degrees(math.acos((dist3 * dist3 - dist2 * dist2 - dist1 * dist1) / (-2 * dist2 * dist1)))
        self.canvas.create_text(self.p1.getX(), self.p1.getY(), text = str(round(angle1, 2)), tags = "angles")
        self.canvas.create_text(self.p2.getX(), self.p2.getY(), text = str(round(angle2, 2)), tags = "angles")
        self.canvas.create_text(self.p3.getX(), self.p3.getY(), text = str(round(angle3, 2)), tags = "angles")
        

    
            
        
        
        
        

        
        

TriAngles()

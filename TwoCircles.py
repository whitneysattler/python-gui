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
        self.points = {"circle1":self.p1, "circle2":self.p2}
        self.radius = 50
        self.small = 1

        item1 = self.canvas.create_oval(self.p1.getX() - self.radius, self.p1.getY() - self.radius, self.p1.getX() + self.radius, self.p1.getY() + self.radius, fill = "red", tags = "circle1")
        item2 = self.canvas.create_oval(self.p2.getX() - self.radius, self.p2.getY() - self.radius, self.p2.getX() + self.radius, self.p2.getY() + self.radius, fill = "red", tags = "circle2")
        item3 = self.canvas.create_oval(self.p1.getX() - self.small, self.p1.getY() - self.small, self.p1.getX() + self.small, self.p1.getY() + self.small, fill = "black", tags = "circle1")
        item4 = self.canvas.create_oval(self.p2.getX() - self.small, self.p2.getY() - self.small, self.p2.getX() + self.small, self.p2.getY() + self.small, fill = "black", tags = "circle2")
        self.canvas.create_line(self.p1.getX(), self.p1.getY(), self.p2.getX(), self.p2.getY(), tags = "line")
        self.canvas.create_text(self.p1.getX(), self.p1.getY() - 60, text = "(" + str(self.p1.getX()) + "," + str(self.p1.getY()) + ")", tags = "text")
        self.canvas.create_text(self.p2.getX(), self.p2.getY() - 60, text = "(" + str(self.p2.getX()) + "," + str(self.p2.getY()) + ")", tags = "text")
        self.canvas.create_text(min(self.p1.getX(), self.p2.getX()) + abs(self.p1.getX() - self.p2.getX())/2, min(self.p1.getY(), self.p2.getY()) + abs(self.p1.getY() - self.p2.getY())/2 - 10, text = format(self.p1.distance(self.p2), ".2f"), tags = "text")


        self.oldX = 0
        self.oldY = 0

        self.canvas.tag_bind("circle1", "<Button-1>", self.clickCircle)
        self.canvas.tag_bind("circle1", "<B1-Motion>", self.dragCircle)
        self.canvas.tag_bind("circle2", "<Button-1>", self.clickCircle)
        self.canvas.tag_bind("circle2", "<B1-Motion>", self.dragCircle)
        
        window.mainloop()

    def clickCircle(self, event):
        self.oldX = event.x
        self.oldY = event.y

    def dragCircle(self, event):
        self.canvas.delete("line", "text")
        dX = event.x - self.oldX
        dY = event.y - self.oldY
        self.canvas.move(self.canvas.gettags(CURRENT)[0], dX, dY)
        point = self.points[self.canvas.gettags(CURRENT)[0]]
        point.setX(point.getX() + dX)
        point.setY(point.getY() + dY)
        self.oldX = event.x
        self.oldY = event.y
        self.canvas.create_line(self.p1.getX(), self.p1.getY(), self.p2.getX(), self.p2.getY(), tags = "line")
        self.canvas.create_text(self.p1.getX(), self.p1.getY() - 60, text = "(" + str(self.p1.getX()) + "," + str(self.p1.getY()) + ")", tags = "text")
        self.canvas.create_text(self.p2.getX(), self.p2.getY() - 60, text = "(" + str(self.p2.getX()) + "," + str(self.p2.getY()) + ")", tags = "text")
        self.canvas.create_text(min(self.p1.getX(), self.p2.getX()) + abs(self.p1.getX() - self.p2.getX())/2, min(self.p1.getY(), self.p2.getY()) + abs(self.p1.getY() - self.p2.getY())/2 - 10, text = format(self.p1.distance(self.p2), ".2f"), tags = "text")
        

TwoCircles()

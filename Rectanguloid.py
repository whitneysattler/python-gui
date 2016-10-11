from tkinter import *
from Point import *

class Rectanguloid:
    def __init__(self, p1, p2):
        window = Tk()
        window.title("Rectanguloid")

        changeX = 25
        changeY = 40

        canvas = Canvas(window, width = 200, height = 250, bg = "white")
        canvas.pack()

        canvas.create_rectangle(p1.getX(), p1.getY(), p2.getX(), p2.getY())
        canvas.create_rectangle(p1.getX() + changeX, p1.getY() + changeY, p2.getX() + changeX, p2.getY() + changeY)
        canvas.create_line(p1.getX(), p1.getY(), p1.getX() + changeX, p1.getY() + changeY)
        canvas.create_line(p1.getX(), p2.getY(), p1.getX() + changeX, p2.getY() + changeY)
        canvas.create_line(p2.getX(), p1.getY(), p2.getX() + changeX, p1.getY() + changeY)
        canvas.create_line(p2.getX(), p2.getY(), p2.getX() + changeX, p2.getY() + changeY)

Rectanguloid(Point(10, 75), Point(125, 175))

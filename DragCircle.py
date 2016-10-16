from tkinter import *

class dragCircles:
    def __init__(self):
        window = Tk()
        window.title("Dragging the Blue Circle")

        self.canvas = Canvas(window, width = 600, height = 300, bg = "white")
        self.canvas.pack()
        radius = 75
        self.canvas.create_oval(300-radius, 100-radius, 300+radius, 100+radius, fill = "black", tags = "circle black")
        self.canvas.create_oval(100-radius, 100-radius, 100+radius, 100+radius, fill = "blue", tags = "circle blue")
        self.canvas.create_oval(500-radius, 100-radius, 500+radius, 100+radius, fill = "red", tags = "circle red")
        self.canvas.create_oval(400-radius, 175-radius, 400+radius, 175+radius, fill = "yellow", tags = "circle yellow")
        self.canvas.create_oval(200-radius, 175-radius, 200+radius, 175+radius, fill = "white", tags = "circle white")
        self.oldX = 0
        self.oldY = 0
        self.canvas.tag_bind("circle", "<Button-1>", self.clickCircle)
        self.canvas.tag_bind("circle", "<B1-Motion>", self.dragCircle)
        self.canvas.tag_bind("circle", "<Double-Button-1>", self.doubleClick)

        window.mainloop

    def dragCircle(self, event):
        deltaX = event.x - self.oldX
        deltaY = event.y - self.oldY
        self.canvas.move(CURRENT, deltaX, deltaY)
        self.oldX = event.x
        self.oldY = event.y
        return

    def clickCircle(self,event):
        self.oldX = event.x
        self.oldY = event.y

    def doubleClick(self, event):
        self.canvas.tag_raise(CURRENT)
    
dragCircles()

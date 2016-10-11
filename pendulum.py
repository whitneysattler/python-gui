from tkinter import *
from math import *

class Pendulum:
    def __init__(self):
        window = Tk()
        window.title("Pendulum")

        self.canvas = Canvas(window, width = 700, height = 500, bg = "white")
        self.canvas.pack()
        self.angle = 270
        self.radius = 450
        self.dx = 1
        self.sleep = 100
        self.sleepDelta = 0
        self.stop = False
        self.drawPendulum()
        self.canvas.bind("<Key>", self.clickControl)
        self.canvas.focus_set()
        
        self.animate()

        window.mainloop()

    def drawPendulum(self):
        self.canvas.delete("Pendulum")
        topCenterX = 350
        topCenterY = 30
        smallRad = 5
        self.canvas.create_oval(topCenterX - smallRad, topCenterY - smallRad, topCenterX + smallRad, topCenterY + smallRad, tags = "Pendulum", fill = "black")
        bigCenterX = cos(radians(self.angle)) * self.radius + topCenterX
        bigCenterY = topCenterY - sin(radians(self.angle))* self.radius 
        self.canvas.create_line(topCenterX, topCenterY, bigCenterX, bigCenterY, tags = "Pendulum")
        self.canvas.create_oval(bigCenterX - 10, bigCenterY - 10, bigCenterX + 10, bigCenterY + 10, tags = "Pendulum", fill = "black")

    def animate(self):
        while (not self.stop):
            self.angle += self.dx
            if self.angle == 310:
                self.dx = -1
            elif self.angle == 230:
                self.dx = 1
            self.sleep = 100 + self.sleepDelta
            self.drawPendulum()
            self.canvas.after(self.sleep)
            self.canvas.update()

    def clickControl(self, event):
        print (event.keysym)
        if event.keysym == "s":
            self.stop = True
        elif event.keysym == "r":
            self.stop = False
            self.animate()
        elif event.keysym == "Up":
            if self.sleepDelta >= -90:
                self.sleepDelta -= 5
        elif event.keysym == "Down":
            if self.sleepDelta <= 90:
                self.sleepDelta += 5
            

Pendulum()

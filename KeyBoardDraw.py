from tkinter import *

class Snake:
    def __init__(self):
        window = Tk()
        window.title("Arrow Keys")

        self.canvas = Canvas(window, height = 300, width = 500, bg = "white")
        self.canvas.pack()

        self.startX = 250
        self.startY = 150
        self.endX = 250
        self.endY = 150

        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()
        self.direction = ""
        
        while True:
            self.drawStep()
            self.canvas.after(50)
            self.canvas.update()
            
        window.mainloop()

    def processKeyEvent(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym
            
    def drawStep(self):
        if self.direction == "Up":
            self.endY -= 10
        elif self.direction == "Left":
            self.endX -= 10
        elif self.direction == "Right":
            self.endX += 10
        elif self.direction == "Down":
            self.endY += 10

        self.canvas.create_line(self.startX, self.startY, self.endX, self.endY)
        self.startX = self.endX
        self.startY = self.endY

Snake()

        


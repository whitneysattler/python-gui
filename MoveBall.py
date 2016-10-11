from tkinter import *

class MoveBall:
    def __init__(self):
        window = Tk()
        window.title("Moving Ball")

        self.canvas = Canvas(window, bg = "white", height = 200, width = 200)
        self.canvas.pack()

        # Create ball on canvas
        self.x = 100
        self.y = 100
        self.dx = 10
        self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, tags = "ball", fill = "red")
        

        frame1 = Frame(window)
        frame1.pack()

        # Create movement buttons
        leftBtn = Button(frame1, text = "Left", command = self.moveLeft)
        leftBtn.pack(side = LEFT)
        rightBtn = Button(frame1, text = "Right", command = self.moveRight)
        rightBtn.pack(side = LEFT)
        upBtn = Button(frame1, text = "Up", command = self.moveUp)
        upBtn.pack(side = LEFT)
        downBtn = Button(frame1, text = "Down", command = self.moveDown)
        downBtn.pack(side = LEFT)

        window.mainloop()

    def moveLeft(self):
        self.canvas.delete("ball")
        if self.x >= 20:
            self.x -= self.dx
        self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, tags = "ball", fill = "red")
            

    def moveRight(self):
        self.canvas.delete("ball")
        if self.x <= 180:
            self.x += self.dx
        self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, tags = "ball", fill = "red")
            

    def moveUp(self):
        self.canvas.delete("ball")
        if self.y >= 20:
            self.y -= self.dx
        self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, tags = "ball", fill = "red")
    

    def moveDown(self):
        self.canvas.delete("ball")
        if self.y <= 180:
            self.y += self.dx
        self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, tags = "ball", fill = "red")
            

MoveBall()

from tkinter import *

class RacingCar:
    def __init__(self):
        window = Tk()
        window.title("Racing Car")

        self.canvas = Canvas(window, width = 400, height = 100, bg = "white")
        self.canvas.pack()

        self.x = 0
        self.y = 65
        self.speed = 10
        wait = 100

        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        while True:
            self.x += self.speed
            if (self.x > int(self.canvas["width"]) - 50):
                self.x = 0
            self.drawCar()
            self.canvas.update()
            self.canvas.after(wait)

        window.mainloop()
        
    def drawCar(self):
        self.canvas.delete("car")
        self.canvas.create_oval(self.x + 10, self.y - 10, self.x + 20, self.y, fill = "black", tags = "car")
        self.canvas.create_oval(self.x + 30, self.y - 10, self.x + 40, self.y, fill = "black", tags = "car")
        self.canvas.create_rectangle(self.x, self.y-20, self.x + 50, self.y - 10, fill = "red", tags = "car")
        self.canvas.create_polygon(self.x + 10, self.y - 20, self.x + 20, self.y - 30, self.x + 30, self.y - 30, self.x + 40, self.y - 20, fill = "blue", tags = "car")

    def processKeyEvent(self, event):
        print (event.keysym)
        if event.keysym == "Up":
            self.speed += 5
        elif event.keysym == "Down":
            self.speed -= 5

RacingCar()

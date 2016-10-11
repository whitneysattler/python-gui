from tkinter import *

class CircleMover:
    def __init__(self):
        window = Tk()
        window.title("Moving Circle")

        self.canvas = Canvas(window, width = 300, height = 250, bg = "white")
        self.canvas.pack()

        self.radius = 10
        self.center = [150, 125]

        self.canvas.create_oval(self.center[0] - self.radius, self.center[1] - self.radius, \
                                self.center[0] + self.radius, self.center[1] + self.radius, \
                                tags = "circle")
        
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()
        window.mainloop()

    def processKeyEvent(self, event):
        x = 0
        y = 0
        if event.keysym == "Up" and self.center[1] > 15:
            y = -10
            self.center[1] -= 10
        elif event.keysym == "Down" and self.center[1] < 235:
            y = 10
            self.center[1] += 10
        elif event.keysym == "Left" and self.center[0] > 15:
            x = -10
            self.center[0] -= 10
        elif event.keysym == "Right" and self.center[0] < 290:
            x = 10
            self.center[0] += 10
        self.canvas.move("circle", x, y)
        self.canvas.update()

CircleMover()

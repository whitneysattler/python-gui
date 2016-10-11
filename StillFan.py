from tkinter import *

class StillFan:
    def __init__(self):
        window = Tk()
        window.title("Still Fan")

        self.canvas = Canvas(window, width = 300, height = 300, bg = "white")
        self.canvas.pack()
        self.begin = 0
        self.colorIndex = 0

        while True:
            self.drawBlades()
            self.canvas.after(1)
            self.canvas.update()

        window.mainloop

    def drawBlades(self):
        colors = ["green", "blue", "red", "orange", "purple", "black", "yellow"]
        self.canvas.delete("blades")
        for i in range(4):
            self.canvas.create_arc(25, 25, 275, 275, start = self.begin + i * 90, extent = 30, fill = colors[self.colorIndex], tag = "blades")
        self.begin = (self.begin + 10) % 360
        self.colorIndex = (self.colorIndex + 1) % len(colors)

StillFan()

from tkinter import *

class Grid:
    def __init__(self):
        window = Tk()
        window.title("Display Grid")

        gridSize = 75
        self.canvas = Canvas(window, width = gridSize * 8, height = gridSize * 8, bg = "white")
        self.canvas.pack()

        for i in range(1, 8):
            self.canvas.create_line(i * gridSize, 0, i * gridSize, 8 * gridSize, fill = "red", tags = "line")
            self.canvas.create_line(0, i * gridSize, 8 * gridSize, i * gridSize, fill = "blue", tags = "line")

        window.mainloop()

Grid()

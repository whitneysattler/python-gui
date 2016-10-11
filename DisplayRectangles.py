from tkinter import *

class DisplayRectangles:
    def __init__(self):
        window = Tk()
        window.title("Display Rectangles")

        self.canvas = Canvas(window, bg = "white", width = 250, height = 200)
        self.canvas.pack()
        for i in range(20):
            self.canvas.create_rectangle(10+4*i,10+4*i, 240-4*i, 190-4*i)

        window.mainloop()
        
DisplayRectangles()

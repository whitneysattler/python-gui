from tkinter import *

class MouseClicker:
    def __init__(self):
        window = Tk()
        window.title("Mouse Position")

        self.canvas = Canvas(window, height = 100, width = 250, bg = "white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.processMouseEvent)

        window.mainloop()

    def processMouseEvent(self, event):
        self.canvas.delete("location")
        self.canvas.create_text(event.x, event.y, text = "(" + str(event.x) + ", " + str(event.y) + ")", tags = "location")

class MouseDragger:
    def __init__(self):
        window = Tk()
        window.title("Mouse Position")

        self.canvas = Canvas(window, height = 100, width = 250, bg = "white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.onMouseClick)
        self.canvas.bind("<ButtonRelease-1>", self.onMouseRelease)

        window.mainloop()

    def onMouseClick(self, event):
        self.canvas.create_text(event.x, event.y, text = "(" + str(event.x) + ", " + str(event.y) + ")", tags = "location")

    def onMouseRelease(self, event):
        self.canvas.delete("location")
MouseDragger()


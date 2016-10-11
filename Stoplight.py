from tkinter import *

class Stoplight:
    def __init__(self):
        window = Tk()
        window.title("Stoplight")

        wid = 300
        hgt = 630
        self.radius = 75
        self.canvas = Canvas(window, width = wid, height = hgt, bg = "white")
        self.canvas.pack()

        self.circles = [(75, 70), (75, 240), (75, 410)]
        self.canvas.create_rectangle(50, 50, wid - 50, hgt - 50, fill = "black")
        for bunch in self.circles:
            self.canvas.create_oval(bunch[0], bunch[1], bunch[0] + self.radius * 2, bunch[1] + self.radius * 2, fill = "white")
        frame1 = Frame(window)
        frame1.pack()
        

        self.color = StringVar()
        Radiobutton(frame1, text = "Green", variable = self.color, value = "green", command = self.processRadio).pack(side = LEFT)
        Radiobutton(frame1, text = "Yellow", variable = self.color, value = "yellow", command = self.processRadio).pack(side = LEFT)
        Radiobutton(frame1, text = "Red", variable = self.color, value = "red", command = self.processRadio).pack(side = LEFT)
        window.mainloop()

    def processRadio(self):
        if self.color.get() == "green":
            self.drawLight(0)
        elif self.color.get() == "yellow":
            self.drawLight(1)
        else:
            self.drawLight(2)

    def drawLight(self, num):
        self.canvas.delete("lights")
        self.canvas.create_oval(self.circles[num][0], self.circles[num][1], self.circles[num][0] + self.radius * 2, self.circles[num][1] + self.radius * 2, fill = self.color.get(), tags = "lights")

Stoplight()

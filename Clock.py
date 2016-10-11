from tkinter import *
from datetime import datetime
from math import *

class Clock:
    def __init__(self):

        window = Tk()
        window.title("Current Time")
        
        self.tall = 400
        self.wide = 400
        self.radius = 150
        self.hourLength = 75
        self.minuteLength = 105
        self.secondLength = 120

        self.canvas = Canvas(window, height = self.tall, width = self.wide, bg = "white")
        self.canvas.pack()
        self.canvas.create_oval(self.wide/2 - self.radius, self.tall/2 - self.radius, self.wide/2 + self.radius, self.tall/2 + self.radius)
        self.canvas.create_text(self.wide/2, self.tall/2 - (self.radius - 7), text = "12")
        self.canvas.create_text(self.wide/2 + (self.radius - 7), self.tall/2, text = "3")
        self.canvas.create_text(self.wide/2, self.tall/2 + (self.radius - 7), text = "6")
        self.canvas.create_text(self.wide/2 - (self.radius - 7), self.tall/2, text = "9")

        self.drawHands()
        while True:
           self.canvas.update()
           self.canvas.after(1000)
           self.drawHands()

        window.mainloop()

    def drawHands(self):
        currentTime = datetime.now().time()
        self.canvas.delete("line")
        self.canvas.create_line(self.wide/2, self.tall/2, self.wide/2 + sin(radians(6 * currentTime.second)) * self.secondLength, \
                                self.tall/2 - cos(radians(6 * currentTime.second)) * self.secondLength, tags = "line")
        self.canvas.create_line(self.wide/2, self.tall/2, self.wide/2 + sin(radians((currentTime.second + currentTime.minute * 60) / 10)) * self.minuteLength, \
                                self.tall/2 - cos(radians((currentTime.second + currentTime.minute * 60) / 10)) * self.minuteLength, fill = "blue", tags = "line")
        self.canvas.create_line(self.wide/2, self.tall/2, self.wide/2 + sin(radians((currentTime.second + currentTime.minute * 60 + (currentTime.hour % 12) * 3600) / 120)) * self.hourLength, \
                                self.tall/2 - cos(radians((currentTime.second + currentTime.minute * 60 + (currentTime.hour % 12) * 3600) / 120)) * self.hourLength, fill = "red", tags = "line")
        self.canvas.create_text(self.wide/2, self.tall/2 + self.radius + 10, text = str(currentTime.hour) + ":" + str(currentTime.minute) + ":" + format(currentTime.second, "2d"), tags = "line")

Clock()

from tkinter import *
from math import *

class BarChart:
    def __init__(self, gradeDist):
        window = Tk()
        window.title("Pie Chart")

        tall = 400
        wide = 400
        radius = 150
        self.canvas = Canvas(window, height = tall, width = wide, bg = "white")
        self.canvas.pack()

        place = 0

        for elt in gradeDist:
            self.canvas.create_arc((wide / 2) - radius, (tall / 2) - radius, (wide / 2) + radius, (tall / 2) + radius, start = place, extent = 3.6 * elt[1], fill = elt[2])
            mid = place + (3.6 * elt[1] / 2)
            place += 3.6 * elt[1]
            self.canvas.create_text((wide / 2) + cos(radians(mid)) * radius, (tall  / 2) - sin(radians(mid)) * radius, text = elt[0] + " -- " + str(elt[1]) + "%")

        window.mainloop()
BarChart([("Project", 20, "red"), ("Quizzes", 10, "blue"), ("Midterm", 30, "green"), ("Final", 40, "orange")])

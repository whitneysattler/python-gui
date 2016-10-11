from tkinter import *

class BarChart:
    def __init__(self, gradeDist):
        window = Tk()
        window.title("Bar Chart")

        self.canvas = Canvas(window, height = 400, width = 800, bg = "white")
        self.canvas.pack()

        barNums = len(gradeDist)
        
        barWidth = (int(self.canvas["width"]) - ((barNums + 1) * 20))/barNums

        self.canvas.create_line(5, int(self.canvas["height"]) - 50, int(self.canvas["width"]) - 5, int(self.canvas["height"]) - 50)
        place = 0

        for elt in gradeDist:
            place += 20
            self.canvas.create_rectangle(place, 350 - elt[1] * 3.5, place + barWidth, 350, fill = elt[2])
            self.canvas.create_text(place + (barWidth / 2), (350 - elt[1] * 350 / 100) - 10, text = elt[0] + " -- " + str(elt[1]) + "%")
            place += barWidth
        window.mainloop()

BarChart([("Project", 20, "red"), ("Quizzes", 10, "blue"), ("Midterm", 30, "green"), ("Final", 40, "orange")])

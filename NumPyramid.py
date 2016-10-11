from tkinter import *

class NumberPyramid:
    def __init__(self):
        self.window = Tk()
        self.window.title("Pyramid")

        tall = 150
        row = 150
        self.canvas = Canvas(self.window, width = row, height = tall, bg = "white")
        self.canvas.pack(fill = BOTH, expand = YES)

        for i in range(1,12):
            s = ""
            for j in range(1, i + 1):
                s += str(j) + " "
            self.canvas.create_text(row / 2, i * tall / 12, text = s, fill = "red", tags = "nums")
        self.change = True
            
        self.canvas.bind("<Configure>", self.configure)

        self.window.mainloop()
        

    def configure(self, event):
        self.canvas.delete("nums")
        
        tall = event.height

        numRows = int(tall / 12.5)
        for i in range(1, numRows):
            s = ""
            for j in range(1, i + 1):
                s += str(j) + " "
            self.canvas.create_text(event.width / 2, (i)*12.5, text = s, fill = "red", tags = "nums")
        
NumberPyramid()

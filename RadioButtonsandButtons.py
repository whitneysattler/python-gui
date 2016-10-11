from tkinter import *

class Radio:
    def __init__(self):
        window = Tk()
        window.title("Radio Buttons and Buttons")

        frame1 = Frame(window)
        frame1.pack()
    
        self.color = StringVar()

        Radiobutton(frame1, text = "Red", variable = self.color, value = "red", command = self.processRadio).pack(side = LEFT)
        Radiobutton(frame1, text = "Yellow", variable = self.color, value = "yellow", command = self.processRadio).pack(side = LEFT)
        whiteButton = Radiobutton(frame1, text = "White", variable = self.color, value = "white", command = self.processRadio)
        whiteButton.pack(side = LEFT)
        Radiobutton(frame1, text = "Gray", variable = self.color, value = "gray", command = self.processRadio).pack(side = LEFT)
        Radiobutton(frame1, text = "Green", variable = self.color, value = "green", command = self.processRadio).pack(side = LEFT)
        frame1.update()
        
        self.canvas = Canvas(window, width = frame1.winfo_width(), height = 50, bg = "white")
        self.canvas.create_text(frame1.winfo_width() / 2, 25, text = "Welcome", tags = "words")
        self.canvas.pack()
        whiteButton.invoke()

    
        frame2 = Frame(window)
        frame2.pack()
        
        Button(frame2, text = "<=", command = self.moveLeft).pack(side = LEFT)
        Button(frame2, text = "=>", command = self.moveRight).pack(side = LEFT)

        self.dx = 5
        window.mainloop()

    def processRadio(self):
        self.canvas["bg"] = self.color.get()
        self.canvas.update()

    def moveLeft(self):
        self.canvas.move("words", -1 * self.dx, 0)
        self.canvas.update()

    def moveRight(self):
        self.canvas.move("words", self.dx, 0)
        self.canvas.update()

Radio()

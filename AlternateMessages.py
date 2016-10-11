from tkinter import *

class Message:
    def __init__(self, messages):
        window = Tk()
        window.title("Rotating Message")

        self.messages = messages

        self.canvas = Canvas(window, height = 250, width = 300, bg = "white")
        self.canvas.pack(fill = Y)

        self.index = 0

        self.canvas.create_text(150, 125, text = self.messages[self.index], tags = "words")

        self.canvas.bind("<Button-1>", self.processMouseEvent)

        window.mainloop()

    def processMouseEvent(self, event):
        self.canvas.delete("words")

        self.index = (self.index + 1) % len(self.messages)
        self.canvas.create_text(150,125, text = self.messages[self.index], tags = "words")

Message(["Programming is fun", "It is fun to program", "I sure like programming"])


        

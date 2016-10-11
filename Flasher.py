from tkinter import *

class TextFlash:
    def __init__(self):
        root = Tk()
        root.title("Flashing Text")

        self.canvas = Canvas(root, height = 200, width = 300, bg = "white")
        self.canvas.pack()
        self.on = True

        while True:
            if self.on:
                self.canvas.create_text(150, 100, text = "Welcome!", tags = "flash")
            else:
                self.canvas.delete("flash")
            self.on = not(self.on)
            self.canvas.after(100)
            self.canvas.update()

        root.mainloop()

    
TextFlash()
                

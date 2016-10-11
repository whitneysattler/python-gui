from tkinter import * # Import al definitions from tkinter

class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        window.title("Event Demo")
        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()

        # Bing with <Button-1> event
        self.canvas.bind("<Button-1>", self.processMouseEvent)

        # Bind with <Key> event
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        window.mainloop() # Create an event loop

    def processMouseEvent(self, event):
        print("clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button is clicked? ", event.num)

    def processKeyEvent(self, event):
        print("keysym? ", event.keysym)
        print("char? ", event.char)
        print("keycode? ", event.keycode)

MouseKeyEventDemo() # Create GUI

from tkinter import * # Import all definitions from tkinter

class CanvasDemo():
    def __init__(self):
        window = Tk() # Create a window
        window.title("Canvas Demo") # Set a title

        # Place the canvas in the window
        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()

        # Place buttons in frame
        frame = Frame(window)
        frame.pack()
        btRectangle = Button(frame, text = "Rectangle", command = self.displayRect)
        btOval = Button(frame, text = "Oval", command = self.displayOval)
        btArc = Button(frame, text = "Arc", command = self.displayArc)
        btPoly = Button(frame, text = "Polygon", command = self.displayPoly)
        btLine = Button(frame, text = "Line", command = self.displayLine)
        btString = Button(frame, text = "String", command = self.displayString)
        btClear = Button(frame, text = "Clear", command = self.clearCanvas)
        btRectangle.grid(row = 1, column = 1)
        btOval.grid(row = 1, column = 2)
        btArc.grid(row = 1, column = 3)
        btPoly.grid(row = 1, column = 4)
        btLine.grid(row = 1, column = 5)
        btString.grid(row = 1, column = 6)
        btClear.grid(row = 1, column = 7)

        window.mainloop() # Create an event loop

    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill = "red", tags = "oval")

    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 8, fill = "red", tags = "arc")

    def displayPoly(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")

    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill = "red", tags = "line")
        self.canvas.create_line(10, 90, 190, 10, width = 9, arrow = "last", activefill = "blue", tags = "line")

    def displayString(self):
        self.canvas.create_text(60, 40, text = "Hi, I am a string", font = "Times 10 bold underline", tags = "string")

    # Clear Drawings
    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

CanvasDemo() # Create GUI

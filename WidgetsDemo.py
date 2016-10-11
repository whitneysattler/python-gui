from tkinter import * # Import all definitions from tkinter

class WidgetsDemo():
    def __init__(self):
        window = Tk() # Create a window
        window.title("Widgets Demo") # Set a title

        # Add a check button and a radio button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red", variable = self.v2, value = 1, command = self.processRadioButton)
        rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow", variable = self.v2, value = 2, command = self.processRadioButton)
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)

        # Add a label, an entry, a button , and a message to frame1
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text = "Get Name", command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)

        # Add text
        self.text = Text(window, font = "Courier 15") # Create and add text to the window
        self.text.pack()
        self.text.insert(END, "Tip\nThe best way to learn Tkinter is to read \nthese carefully designed examples and use them \nto create your applications.")

        window.mainloop() # Create an event loop

    def processCheckbutton(self):
        print("Check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))
        if self.v1.get() == 1:
            self.text["font"] = "Courier 15 bold"
        else:
            self.text["font"] = "Courier 15"

    def processRadioButton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected")
        if self.v2.get() == 1:
            self.text["bg"] = "red"
        elif self.v2.get() == 2:
            self.text["bg"] = "yellow"

    def processButton(self):
        self.text.insert(END, (self.name.get() + " ")*5)

WidgetsDemo() # Create GUI

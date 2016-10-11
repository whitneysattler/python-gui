from tkinter import * #Import all definitions from tkinter

class ChangeLabelDemo():
    def __init__(self):
        window = Tk() # Create a window
        window.title("Change Label Demo") # Set a title

        # Add a label to frame1
        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text = "Programming is fun")
        self.lbl.pack()

        # Add a label, entry, button, two radio buttons to frame2
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Enter text: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable=self.msg)
        btChangeTxt = Button(frame2, text = "Change Text", command = self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Red", bg = "red", variable = self.v1, value = "R", command = self.processRadioButton)
        rbYellow = Radiobutton(frame2, text = "Yellow", bg = "yellow", variable = self.v1, value = "Y", command = self.processRadioButton)

        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeTxt.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)

        window.mainloop() # Create an event loop

    def processButton(self):
        self.lbl["text"] = self.msg.get()

    def processRadioButton(self):
        if self.v1.get() == "R":
            self.lbl["fg"] = "red"
        elif self.v1.get() == "Y":
            self.lbl["fg"] = "yellow"

ChangeLabelDemo() # Create GUI
        
        

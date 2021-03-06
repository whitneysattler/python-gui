from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window = Tk() # Create a window
        btOK = Button(window, text = "OK", fg = "red", command = self.processOK)
        btCancel = Button(window, text = "Cancel", fg = "yellow", command = self.processCancel)
        btOK.pack() # Place the OK button in the window
        btCancel.pack() # Place the Cancel button in the window

        window.mainloop() # Create an event loop

    def processOK(self):
        print("OK button is clicked")

    def processCancel(self):
        print("Cancel button is clicked")

ProcessButtonEvent()

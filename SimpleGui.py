from tkinter import *

window = Tk() # Create a window
label = Label(window, text = "Welcome to Python")# Create a label
button = Button(window, text = "Click Me") # Create a button
label.pack() # Place a label in the window
button.pack() # Place a button in the window

window.mainloop() # Create an event loop

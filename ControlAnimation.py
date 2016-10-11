from tkinter import *

class ControlAnimation:
    def __init__(self):
        window = Tk()
        window.title("Control Animation Demo")

        self.width = 250 # width of self.canvas
        self.canvas = Canvas(window, bg = "white", width = 250, height = 50)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume", command = self.resume)
        btResume.pack(side = LEFT)
        btFaster = Button(frame, text = "Faster", command = self.faster)
        btFaster.pack(side = LEFT)
        btSlower = Button(frame, text = "Slower", command = self.slower)
        btSlower.pack(side = LEFT)

        self.x = 0 # Starting x position
        self.sleepTime = 100 # Set a sleep time
        self.canvas.create_text(self.x, 30, text = "Message moving?", tags = "text")

        self.dx = 3
        self.isStopped = False
        self.animate()

        window.mainloop() # Create an event loop

    def stop(self): # Stop animation
        self.isStopped = True

    def resume(self): # Resume animation
        self.isStopped = False
        self.animate()

    def faster(self): # Speed up the animation
        if self.sleepTime > 5:
            self.sleepTime -= 5
        elif self.sleepTime >1:
            self.sleepTime -= 1

    def slower(self): # Slow downt the animation
        self.sleepTime += 20

    def animate(self):
        while not self.isStopped:
            self.canvas.move("text", self.dx, 0) # Move text
            self.canvas.after(self.sleepTime) # Sleep
            self.canvas.update() # Update canvas
            if self.x < self.width:
                self.x += self.dx # Set new position
            else:
                self.x = 0 # reset position of string
                self.canvas.delete("text")
                # Redraw text at the beginning
                self.canvas.create_text(self.x, 30, text = "Message moving?", tags = "text")

ControlAnimation() # Create GUI

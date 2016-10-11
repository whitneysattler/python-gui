from tkinter import * # Import all definitions from tkinter

class ImageDemo:
    def __init__(self):
        window = Tk()
        window.title("Image Demo") # Set title

        # Create PhotoImage objects
        caImage = PhotoImage(file = "image/ca.gif")
        chinaImage = PhotoImage(file = "image/china.gif")
        leftImage = PhotoImage(file = "image/left.gif")
        rightImage = PhotoImage(file = "image/right.gif")
        usImage = PhotoImage(file = "image/usIcon.gif")
        ukImage = PhotoImage(file = "image/ukIcon.gif")
        crossImage = PhotoImage(file = "image/x.gif")
        circleImage = PhotoImage(file = "image/o.gif")

        # frame1 to contain label and canvas
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, image = caImage).pack(side = LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(90, 50, image = chinaImage)
        canvas["width"] = 200
        canvas["height"] = 100
        canvas.pack(side = LEFT)

        # frame2 contains buttons, check buttons, and radio buttons
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, image = leftImage).pack(side = LEFT)
        Button(frame2, image = rightImage).pack(side = LEFT)
        Checkbutton(frame2, image = usImage).pack(side = LEFT)
        Checkbutton(frame2, image = ukImage).pack(side = LEFT)
        self.v2 = IntVar()
        Radiobutton(frame2, image = crossImage, variable = self.v2, value = 1).pack(side = LEFT)
        Radiobutton(frame2, image = circleImage, variable = self.v2, value = 2).pack(side = LEFT)

        window.mainloop()

ImageDemo()
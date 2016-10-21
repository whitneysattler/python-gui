from tkinter import *

class AddressBook:
    def __init__(self, addresses):
        window = Tk()
        window.title("Address Book")
        
        self.book = addresses
        self.id = 0
        
        frame1 = Frame(window)
        self.name = StringVar()
        self.name.set(self.book[self.id]["name"])
        Label(frame1, text = "Name ").pack(side=LEFT, fill=BOTH)
        Entry(frame1, textvariable = self.name).pack(side=LEFT, expand = 1, fill = BOTH)
        
        frame2 = Frame(window)
        self.street = StringVar()
        self.street.set(self.book[self.id]["street"])
        Label(frame2, text = "Street ").pack(side=LEFT)
        Entry(frame2, textvariable = self.street).pack(side=LEFT)

        frame3 = Frame(window)
        self.city = StringVar()
        self.city.set(self.book[self.id]["city"])
        Label(frame3, text = "City ").pack(side=LEFT)
        Entry(frame3, textvariable = self.city).pack(side=LEFT)
        self.state = StringVar()
        self.state.set(self.book[self.id]["state"])
        Label(frame3, text = "State ").pack(side=LEFT)
        Entry(frame3, textvariable = self.state, width = 3).pack(side=LEFT)
        self.zip = StringVar()
        self.zip.set(self.book[self.id]["zip"])
        Label(frame3, text = "ZIP ").pack(side=LEFT)
        Entry(frame3, textvariable = self.zip, width = 6).pack(side=LEFT)

        frame4 = Frame(window)
        Button(frame4, text = "Add", command = self.add).pack(side=LEFT)
        Button(frame4, text = "First", command = lambda: self.goTo(0)).pack(side=LEFT)
        Button(frame4, text = "Previous", command = lambda:self.goTo(self.id - 1)).pack(side = LEFT)
        Button(frame4, text = "Next", command = lambda:self.goTo(self.id + 1)).pack(side=LEFT)
        Button(frame4, text = "Last", command = lambda:self.goTo(len(self.book) - 1)).pack(side = LEFT)

        frame3.grid(row = 3, column = 1)
        frame4.grid(row = 4, column = 1)
        frame2.grid(row = 2, column = 1)
        frame1.grid(row = 1, column = 1)
        window.mainloop()

    def add(self):
        pass

    def goTo(self, index):
        pass
    
AddressBook([{"name":"Whitney Sattler", "street":"2102 Wood Ranch", "city":"San Antonio", "state":"TX", "zip":"78227"}])
                             

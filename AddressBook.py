from tkinter import *

class Address:
    def __init__(self, name, street, city, state, zipCode):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zipCode
        
class AddressBook:
    def __init__(self, addresses = [Address("Whitney Sattler", "2012 Wood Ranch", "San Antonio", "TX", "78227")]):
        window = Tk()
        window.title("Address Book")
        
        self.book = addresses
        self.id = 0

        frame0 = Frame(window)
        frame0.pack()
        
        frame1 = Frame(frame0)
        Label(frame1, text = "Name ").pack()
        Label(frame1, text = "Street ").pack()
        Label(frame1, text = "City ").pack()
        frame1.pack(side=LEFT)

        frame2 = Frame(frame0)
        self.name = StringVar()
        self.name.set(self.book[self.id].name)
        Entry(frame2, textvariable = self.name).pack(fill = X)
        self.street = StringVar()
        self.street.set(self.book[self.id].street)
        Entry(frame2, textvariable = self.street).pack(fill=X)
        frame2.pack(side=LEFT)
        
        frame3 = Frame(frame2)
        self.city = StringVar()
        self.city.set(self.book[self.id].city)
        Entry(frame3, textvariable = self.city).pack(side=LEFT)
        self.state = StringVar()
        self.state.set(self.book[self.id].state)
        Label(frame3, text = "State ").pack(side=LEFT)
        Entry(frame3, textvariable = self.state, width = 3).pack(side=LEFT)
        self.zip = StringVar()
        self.zip.set(self.book[self.id].zip)
        Label(frame3, text = "ZIP ").pack(side=LEFT)
        Entry(frame3, textvariable = self.zip, width = 6).pack(side=LEFT)
        frame3.pack()
        
        frame4 = Frame(window)
        Button(frame4, text = "Add", command = self.add).pack(side=LEFT)
        Button(frame4, text = "First", command = lambda: self.goTo(0)).pack(side=LEFT)
        Button(frame4, text = "Previous", command = lambda:self.goTo((self.id - 1 + len(self.book)) % len(self.book))).pack(side = LEFT)
        Button(frame4, text = "Next", command = lambda:self.goTo((self.id + 1) % len(self.book))).pack(side=LEFT)
        Button(frame4, text = "Last", command = lambda:self.goTo(len(self.book) - 1)).pack(side = LEFT)

        frame4.pack()
        window.mainloop()

    def add(self):
        if self.checkNew():
            newAddress = Address(self.name.get(), self.street.get(), self.city.get(), self.state.get(), self.zip.get())
            self.book += [newAddress]
            messagebox.showinfo("New Address", "You've added another address!  One more friend for you!")
            self.goTo(self.id)
                 
    def checkNew(self):
        if self.name.get() != self.book[self.id].name:
            return True

    def goTo(self, index):
        self.id = index
        self.name.set(self.book[index].name)
        self.street.set(self.book[index].street)
        self.city.set(self.book[index].city)
        self.state.set(self.book[index].state)
        self.zip.set(self.book[index].zip)
        print (self.id)
    
AddressBook()
                             

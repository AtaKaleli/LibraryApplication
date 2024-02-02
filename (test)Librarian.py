from tkinter import *
from tkinter import messagebox


class Librarian(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Librarian Panel")
        self.master.geometry("400x600")

        self.frame1 = Frame(self)
        self.frame1.pack(padx=5, pady=5)

        self.titleLabel = Label(self.frame1, text="Books")
        self.titleLabel.pack(padx=5, pady=5)

        self.frame2 = Frame(self)
        self.frame2.pack(padx=5, pady=5, expand=YES, fill=BOTH)

        bookFile = open("books.txt", "r")
        fileData = bookFile.readlines()[1:]
        bookData = []
        for line in fileData:
            bookData.append(line.strip("\n").split(";"))

        self.bookNames = []
        for bookName in bookData:
            bookTuple = (bookName[1] + " by " + bookName[2], BooleanVar())
            self.bookNames.append(bookTuple)

        for bookName in self.bookNames:
            self.selectBookName = Checkbutton(self.frame2, anchor=W, text=bookName[0], variable=bookName[1])
            self.selectBookName.pack(expand=YES, fill=BOTH, padx=5, pady=5)

        self.frame3 = Frame(self)
        self.frame3.pack(padx=5, pady=5)

        self.dateLabel = Label(self.frame3, text="Date(dd.mm.yyyy):")
        self.dateLabel.pack(side=LEFT, padx=5, pady=5)

        self.dateEntry = Entry(self.frame3, name="date entry")
        self.dateEntry.pack(padx=5, pady=5)

        self.frame4 = Frame(self)
        self.frame4.pack(padx=5, pady=5)

        self.nameLabel = Label(self.frame4, text="Client's name:")
        self.nameLabel.pack(side=LEFT, padx=5, pady=5)

        self.nameEntry = Entry(self.frame4, name="name entry")
        self.nameEntry.pack(padx=5, pady=5)

        self.frame5 = Frame(self)
        self.frame5.pack(padx=5, pady=5)

        self.rentButton = Button(self.frame5, text="Rent", command=self.pressedRent)
        self.rentButton.pack(side=LEFT, padx=5,pady=5)

        self.returnButton = Button(self.frame5, text="Return", command=self.pressedReturn)
        self.returnButton.pack(side=LEFT, padx=5, pady=5)

        self.closeButton = Button(self.frame5, text="Close", command=self.pressedClose)
        self.closeButton.pack(side=LEFT, padx=5, pady=5)

    def pressedRent(self):
        pass

    def pressedReturn(self):
        pass

    def pressedClose(self):
        pass





















window = Librarian()
window.mainloop()
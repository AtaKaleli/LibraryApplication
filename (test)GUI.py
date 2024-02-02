from tkinter import *
from tkinter import messagebox


class Login(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Login")

        self.frame1 = Frame(self)
        self.frame1.pack(padx=5, pady=5)

        self.userNameLbl = Label(self.frame1, text="User name")
        self.userNameLbl.pack(side=LEFT, padx=5, pady=5)

        self.userNameEntry = Entry(self.frame1, name="username")
        self.userNameEntry.pack(padx=5, pady=5)

        self.frame2 = Frame(self)
        self.frame2.pack(padx=5, pady=5)

        self.passwordLbl = Label(self.frame2, text="Password")
        self.passwordLbl.pack(side=LEFT, padx=5, pady=5)

        self.passwordEntry = Entry(self.frame2, name="password", show="*")
        self.passwordEntry.pack(padx=5, pady=5)

        self.frame3 = Frame(self)
        self.frame3.pack(padx=5, pady=5)

        self.loginBtn = Button(self.frame3, text="Login", command=self.buttonPressed)
        self.loginBtn.pack(padx=5, pady=5)

    def buttonPressed(self):
        userName = self.userNameEntry.get()
        password = self.passwordEntry.get()

        userFile = open("users.txt", "r")
        fileData = userFile.readlines()[1:]
        userData = []
        for line in fileData:
            userData.append(line.strip("\n").split(";"))

        userFound = 0
        for data in userData:
            if userName in data and password == data[1]:
                userFound = 1
                if data[2] == "librarian":
                    self.master.destroy()
                    librarianWindow = Librarian()
                    librarianWindow.mainloop()
                elif data[2] == "manager":
                    self.master.destroy()
                    managerWindow = Manager()
                    managerWindow.mainloop()
                else:
                    print("Error!")

        if not userFound:
            messagebox.showinfo("Error", "Invalid login")


#librarian clas
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


#manager class
class Manager(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Manager Panel")
        self.master.geometry("550x250")


        self.frame1 = Frame(self)
        self.frame1.pack(padx=5, pady=5)

        self.reportsLabel = Label(self.frame1, text="REPORTS")
        self.reportsLabel.pack(padx=5, pady=5)

        self.frame2 = Frame(self)
        self.frame2.pack(padx=5, pady=5)

        self.libraryReports = [
            "(1) What is the most rented book overall?",
            "(2) Which librarian has the highest number of operations?",
            "(3) What is the total generated revenue by the library?",
            "(4) What is the average rental period for the 'Harry Potter' book?"
        ]

        self.report = StringVar()
        self.report.set(self.libraryReports[0])

        for report in self.libraryReports:
            self.selectReport = Radiobutton(self.frame2, anchor=W, text=report, variable=self.report, value=report)
            self.selectReport.pack(padx=5, pady=5,expand=YES, fill=BOTH)

        self.frame3 = Frame(self)
        self.frame3.pack(padx=5, pady=5, expand=YES, fill=BOTH)

        self.createButton = Button(self.frame3, text="Create", command=self.pressedCreate)
        self.createButton.pack(side=LEFT, padx=5, pady=5, expand=YES, fill=BOTH)

        self.closeButton = Button(self.frame3, text="Close", command=self.pressedClose)
        self.closeButton.pack(padx=5, pady=5)

    def pressedCreate(self):
        pass

    def pressedClose(self):
        pass


def System():
    window = Login()
    window.mainloop()


if __name__ == "__main__":
    System()

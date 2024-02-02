from tkinter import *
from tkinter import messagebox


def System():
    window = Manager()
    window.mainloop()




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



if __name__ == "__main__":
    System()

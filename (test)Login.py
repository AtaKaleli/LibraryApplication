from tkinter import *
from tkinter import messagebox


class Login(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Login")
        self.master.geometry("250x150")

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
        messagebox.showinfo("Message", "Welcome boss " + userName)



window = Login()
window.mainloop()

# def buttonPressed(self):
    #     userName = self.userNameEntry.get()
    #     password = self.passwordEntry.get()
    #
    #     userFile = open("users.txt", "r")
    #     fileData = userFile.readlines()[1:]
    #     userData = []
    #     for line in fileData:
    #         userData.append(line.strip("\n").split(";"))
    #
    #     userFound = 0
    #     for data in userData:
    #         if userName in data and password == data[1]:
    #             userFound = 1
    #             if data[2] == "librarian":
    #                 self.master.destroy()
    #                 librarianWindow = Librarian()
    #                 librarianWindow.mainloop()
    #             elif data[2] == "manager":
    #                 self.master.destroy()
    #                 managerWindow = Manager()
    #                 managerWindow.mainloop()
    #             else:
    #                 print("Error!")
    #
    #     if not userFound:
    #         messagebox.showinfo("Error", "Invalid login")
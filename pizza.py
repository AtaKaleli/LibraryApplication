from tkinter import *
from tkinter import messagebox


def System():
    window = Login()
    window.mainloop()


class UpdatedRadio(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("UpdatedRB")
        self.master.geometry("400x200")

        self.frame1 = Frame(self)
        self.frame1.pack(padx=5, pady=5)

        self.toppingLabel = Label(self.frame1,text="Toppings: ")
        self.toppingLabel.pack(side=LEFT, padx=5, pady=5)

        #in checkbox, variables should be in tuple format
        #index 0 represents name, index1 represents the BooleanVariable
        self.toppings = [("Cheese",BooleanVar()),("Olive",BooleanVar()),("Mushroom",BooleanVar())]

        for topping in self.toppings:
            self.toppingSelection = Checkbutton(self.frame1, text=topping[0], variable=topping[1])
            self.toppingSelection.pack(side=LEFT, padx=5, pady=5)





        self.frame2 = Frame(self)
        self.frame2.pack(padx=5, pady=5)

        self.btn = Button(self.frame2, text="Order", command=self.buttonPressed)
        self.btn.pack(padx=5, pady=5)

    def buttonPressed(self):
        toppingNames = ""

        for topping in self.toppings:
            if topping[1].get():
                toppingNames += topping[0] + " "

        messagebox.showinfo("Message","Toppings: " + toppingNames)


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

        if userName == "ata" and password == "kaleli":
            self.master.destroy()
            pizzaWindow = PizzaOrder()
            pizzaWindow.mainloop()
        else:
            self.master.destroy()
            updatedWindow = UpdatedRadio()
            updatedWindow.mainloop()




class PizzaOrder(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Pizza Order")
        self.master.geometry("400x200")

        self.frame1 = Frame(self)
        self.frame1.pack(padx=5, pady=5)

        self.sizeLabel = Label(self.frame1, text="Sizes: ")
        self.sizeLabel.pack(side=LEFT, padx=5, pady=5)

        self.pizzaSizes = ["Small", "Medium", "Large"]
        self.size = StringVar()
        self.size.set(self.pizzaSizes[0])

        for size in self.pizzaSizes:
            self.selectSize = Radiobutton(self.frame1, text=size, variable=self.size, value=size)
            self.selectSize.pack(side=LEFT, padx=5, pady=5)

        self.frame2 = Frame(self)
        self.frame2.pack(padx=5, pady=5)

        self.toppingLabel = Label(self.frame2, text="Toppings: ")
        self.toppingLabel.pack(side=LEFT, padx=5, pady=5)

        self.pizzaToppings = [("Cheese",BooleanVar()),("Onion",BooleanVar()),("Pepperoni",BooleanVar())]

        for topping in self.pizzaToppings:
            self.selectTopping = Checkbutton(self.frame2, text=topping[0], variable=topping[1])
            self.selectTopping.pack(side=LEFT, padx=5, pady=5)

        self.frame3 = Frame(self)
        self.frame3.pack(padx=5, pady=5)

        self.orderButton = Button(self.frame3, text="Order", command=self.buttonPressed)
        self.orderButton.pack(padx=5, pady=5)

    def buttonPressed(self):
        pizzaSize = self.size.get()
        pizzaToppings = ""

        for topping in self.pizzaToppings:
            if topping[1].get():
                pizzaToppings += topping[0] + " "

        messagebox.showinfo("Message", "Pizza Size: " + pizzaSize + "\nPizza Toppings: " + pizzaToppings)



if __name__ == "__main__":
    System()

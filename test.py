from tkinter import *
from tkinter import messagebox

class pizzaScreen(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Pizza Order")

        self.frame1 = Frame(self)
        self.frame1.pack(padx= 5, pady=5)

        self.sizeLabel = Label(self.frame1, text = "Size: ")
        self.sizeLabel.pack(side = LEFT, padx = 5, pady= 5)

        self.pizzaSizes = ["Small", "Medium", "Large"]
        self.size = StringVar()
        self.size.set(self.pizzaSizes[0])

        for pizzaSize in self.pizzaSizes:
            self.pizzaSizeSelection = Radiobutton(self.frame1, text = pizzaSize, value = pizzaSize, variable = self.size)
            self.pizzaSizeSelection.pack(side = LEFT, padx = 5, pady = 5)

        self.frame2 = Frame(self)
        self.frame2.pack(padx= 5, pady=5)

        self.ToppingsLabel = Label(self.frame2, text = "Toppings")
        self.ToppingsLabel.pack(side = LEFT, padx = 5, pady=5)

        self.toppings = [("Cheese", BooleanVar()), ("Olive", BooleanVar()), ("Mushrooms", BooleanVar())]

        for topping in self.toppings:
            self.toppingSelection = Checkbutton(self.frame2, text = topping[0], variable = topping[1])
            self.toppingSelection.pack(side = LEFT, padx = 5, pady = 5)

        self.frame3 = Frame(self)
        self.frame3.pack()

        self.button = Button(self.frame3, text = "Order", command=self.buttonPressed)
        self.button.pack(side=LEFT, padx = 5, pady = 5)

    def buttonPressed(self):
        pSize = self.size.get()
        toppings = ""
        for topping in self.toppings:
            if topping[1].get():
                toppings += topping[0] + " "

        messagebox.showinfo("Message", "Size: " + pSize + "\nToppings: " + toppings)

if __name__ == "__main__":
    window = pizzaScreen()
    window.mainloop()# Show our window
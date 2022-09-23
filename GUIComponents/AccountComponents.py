import tkinter as tk

from Classes.CustomerClass import Customer
from Services import CustomerServices
from Services.AccountServices import addAccount


class accountMaker:
    frame: tk.Tk
    selectedCustomer: Customer
    choice: tk.IntVar

    def __init__(self, frame, selectedCustomer):
        self.frame = frame
        self.selectedCustomer = selectedCustomer

    def makeAccount(self):
        if self.selectedCustomer.getAccount() is None:
            if self.selectedCustomer.getType() == "Retail":
                tk.Label(self.frame, text='Please pick the type of account:').place(relx=0.2, rely=0.4, anchor='center')
                self.choice = tk.IntVar()
                var = tk.StringVar()
                var.set("Choice")
                amount = tk.IntVar()
                R1 = tk.Radiobutton(self.frame, text="Checking account", variable=self.choice, value=1,
                                    command=lambda: var.set("Checking"))
                R1.place(relx=0.45, rely=0.4, anchor='center')

                R2 = tk.Radiobutton(self.frame, text="Savings Account", variable=self.choice, value=2,
                                    command=lambda: var.set("Savings"))
                R2.place(relx=0.7, rely=0.4, anchor='center')
                tk.Label(self.frame, text='Please enter the initial amount:').place(relx=0.2, rely=0.5, anchor='center')
                tk.Entry(self.frame, textvariable=amount).place(relx=0.5, rely=0.5, anchor='center')
                tk.Button(self.frame, text="Confirm data",
                          command=lambda: [addAccount(self.selectedCustomer, amount, var.get()),
                                           self.frame.destroy()]).place(
                    relx=0.2, rely=0.65,
                    anchor='center')
            elif self.selectedCustomer.getType() == "Non-Retail":
                amount = tk.StringVar()
                tk.Label(self.frame, text='Please enter the initial amount taken as loan:').place(relx=0.2, rely=0.5,
                                                                                                  anchor='center')
                tk.Entry(self.frame, textvariable=amount).place(relx=0.5, rely=0.5, anchor='center')
                tk.Button(self.frame, text="Confirm data",
                          command=lambda: [addAccount(self.selectedCustomer, amount, "Loan"),
                                           self.frame.destroy()]).place(
                    relx=0.2, rely=0.65,
                    anchor='center')

        else:
            print("This customer already has an account.")


def openAccount(rootWindow: tk.Tk, frame1):
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    customerName = tk.StringVar(frame, value="Pick Customer")
    nonAccountHolderList = []
    customerNameToObjectdict = {}
    for customer in CustomerServices.CustomerList:
        customerNameToObjectdict[customer.getName()] = customer
        nonAccountHolderList.append(customer.getName())

    tk.Label(frame, text='Please pick the customer you want to open an account for:').place(relx=0.2, rely=0.2,
                                                                                            anchor='center')
    customerMenu = tk.OptionMenu(frame, customerName, *nonAccountHolderList)
    customerMenu.place(relx=0.5, rely=0.2, anchor='center')
    tk.Button(frame, text="Confirm",
              command=lambda: accountMaker(frame, accountMaker(frame, customerNameToObjectdict[
                  customerName.get()]).makeAccount())).place(relx=0.2, rely=0.65, anchor='center')

    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

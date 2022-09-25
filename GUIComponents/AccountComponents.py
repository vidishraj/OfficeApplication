import tkinter as tk
from Services.AccountServices import AccountService


class UserAccountGUI:
    frame: tk.Tk
    choice: tk.IntVar
    _rootWindow: tk.Tk
    _AccountService: AccountService

    def __init__(self, rootWindow, frame, userData):
        self.frame = frame
        self._rootWindow = rootWindow
        self._AccountService = AccountService(userData)

    def openAccount(self):
        frame = tk.Frame(self._rootWindow, width=800, height=800)
        frame.grid(row=0, column=0, sticky='news')
        frame.tkraise(self.frame)
        customerName = tk.StringVar(frame, value="Pick Customer")
        nonAccountHolderList = self._AccountService.returnNonAccountNameList()

        tk.Label(frame, text='Please pick the customer you want to open an account for:').place(relx=0.2, rely=0.2,
                                                                                                anchor='center')
        customerMenu = tk.OptionMenu(frame, customerName, *nonAccountHolderList)
        customerMenu.place(relx=0.5, rely=0.2, anchor='center')
        tk.Button(frame, text="Confirm",
                  command=lambda: self.makeAccount(frame, customerName.get())).place(relx=0.2, rely=0.65, anchor='center')
        tk.Button(frame, text="Back",
                  command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

    def makeAccount(self, frame, selectedCustomerName):
        selectedCustomer=self._AccountService.returnCustomerFromName(selectedCustomerName)
        if selectedCustomer.getAccount() is None:
            if selectedCustomer.getType() == "Retail":
                tk.Label(frame, text='Please pick the type of account:').place(relx=0.2, rely=0.4, anchor='center')
                self.choice = tk.IntVar()
                var = tk.StringVar()
                var.set("Choice")
                amount = tk.IntVar()
                R1 = tk.Radiobutton(frame, text="Checking account", variable=self.choice, value=1,
                                    command=lambda: var.set("Checking"))
                R1.place(relx=0.45, rely=0.4, anchor='center')

                R2 = tk.Radiobutton(frame, text="Savings Account", variable=self.choice, value=2,
                                    command=lambda: var.set("Savings"))
                R2.place(relx=0.7, rely=0.4, anchor='center')
                tk.Label(frame, text='Please enter the initial amount:').place(relx=0.2, rely=0.5, anchor='center')
                tk.Entry(frame, textvariable=amount).place(relx=0.5, rely=0.5, anchor='center')
                tk.Button(frame, text="Confirm data",
                          command=lambda: [self._AccountService.addAccount(selectedCustomerName, amount.get(),
                                                                           var.get()),  frame.destroy()]).place(
                    relx=0.2, rely=0.65,
                    anchor='center')
            elif selectedCustomer.getType() == "Non-Retail":
                amount = tk.StringVar()
                tk.Label(frame, text='Please enter the initial amount taken as loan:').place(relx=0.2, rely=0.5,
                                                                                             anchor='center')
                tk.Entry(frame, textvariable=amount).place(relx=0.5, rely=0.5, anchor='center')
                tk.Button(frame, text="Confirm data",
                          command=lambda: [self._AccountService.addAccount(selectedCustomer, amount, "Loan"),
                                           frame.destroy()]).place(
                    relx=0.2, rely=0.65,
                    anchor='center')

        else:
            print("This customer already has an account.")

    def listAccounts(self):
        try:
            frame = tk.Frame(self._rootWindow, width=800, height=800)
            frame.grid(row=0, column=0, sticky='news')
            frame.tkraise(self.frame)
            if len(self._AccountService.returnAccountHolderList()) > 0:
                table = tk.ttk.Treeview(frame)
                table.place(relx=0.5, rely=0.25, anchor='center')
                table['columns'] = ('Name', 'Customer Type', 'Account Type', "Account Number", "Amount", "Interest")
                table.column("#0", width=0, stretch="no")
                table.column("Name", anchor="center", width=150)
                table.column("Customer Type", anchor="center", width=150)
                table.column("Account Type", anchor="center", width=150)
                table.column("Account Number", anchor="center", width=150)
                table.column("Amount", anchor="center", width=50)
                table.column("Interest", anchor="center", width=150)

                table.heading("#0", text="", anchor="center")
                table.heading("Name", text="Name", anchor="center")
                table.heading("Customer Type", text="Customer Type", anchor="center")
                table.heading("Account Type", text="Account Type", anchor="center")
                table.heading("Account Number", text="Account Number", anchor="center")
                table.heading("Amount", text="Amount", anchor="center")
                table.heading("Interest", text="Interest", anchor="center")
                lst = []
                tk.Button(frame, text="Back",
                          command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
                accountDetailsList = self._AccountService.displayMoney()
                total_rows = len(accountDetailsList)
                for i in range(total_rows):
                    table.insert(parent='', index='end', iid=i, text='',
                                 values=accountDetailsList[i])
            else:
                tk.Label(frame, text='There are no customers').place(relx=0.2, rely=0.4, anchor='center')
        except Exception as e:
            print(e)

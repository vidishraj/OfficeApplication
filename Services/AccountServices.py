from random import randint
import tkinter as tk
from Classes.AccountClass import Account
from Services.CustomerServices import CustomerList


def addAccount(Customer, initDeposit, typeOfAccount):
    try:
        accountNumber: int = randint(10000, 99999)
        newAccount: Account = Account(initDeposit, accountNumber, typeOfAccount)
        Customer.setAccount(newAccount)
        print("Account set.")
    except Exception as e:
        print(e)


def displayMoney(rootWindow, frame1):
    try:
        frame = tk.Frame(rootWindow, width=800, height=800)
        frame.grid(row=0, column=0, sticky='news')
        frame.tkraise(frame1)
        if len(CustomerList) > 0:
            accountList = []
            for Customer in CustomerList:
                if Customer.getAccount() is not None:
                    cust = {'name': Customer.getName(), 'customerType': Customer.getType(),
                            'account': Customer.getAccount()}
                    accountList.append(cust.copy())
            print(accountList)
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
            for account in accountList:
                temp = [account['name'], account['customerType'], account['account'].getType(),
                        account['account'].getAccountNumber(), account['account'].latestBalance(),
                        account['account'].latestBalance() - account['account'].getDeposit()]
                lst.append(temp.copy())
            total_rows = len(lst)
            for i in range(total_rows):
                table.insert(parent='', index='end', iid=i, text='',
                             values=lst[i])
        else:
            tk.Label(frame, text='There are no customers').place(relx=0.2, rely=0.4, anchor='center')
    except Exception as e:
        print(e)

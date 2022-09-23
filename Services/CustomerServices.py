from random import randint

from Classes.CustomerClass import Customer
import tkinter as tk
CustomerList = []


def createCustomer(name, age, aadhar, typeOfAccount):
    try:
        newCustomer = Customer(name, age, aadhar, typeOfAccount, None)
        CustomerList.append(newCustomer)
    except Exception as e:
        print(e)



def listCustomers(rootWindow: tk.Tk, frame1):
    lst = []
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    set = tk.ttk.Treeview(frame)
    set.place(relx=0.5, rely=0.25, anchor='center')
    set['columns'] = ('Name', 'Age', 'Aadhar', "Type", "Account Number")
    set.column("#0", width=0, stretch="no")
    set.column("Name", anchor="center", width=150)
    set.column("Age", anchor="center", width=50)
    set.column("Aadhar", anchor="center", width=150)
    set.column("Type", anchor="center", width=80)
    set.column("Account Number", anchor="center", width=150)

    set.heading("#0", text="", anchor="center")
    set.heading("Name", text="Name", anchor="center")
    set.heading("Age", text="Age", anchor="center")
    set.heading("Aadhar", text="Aadhar ", anchor="center")
    set.heading("Type", text="Type", anchor="center")
    set.heading("Account Number", text="Account Number", anchor="center")

    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
    for Customer in CustomerList:
        accountNumber = 0
        if Customer.getAccount() is not None:
            accountNumber = Customer.getAccount().getAccountNumber()

        temp = [Customer.getName(), Customer.getAge(), Customer.getAadhar(), Customer.getType(), accountNumber]
        lst.append(temp)

    total_rows = len(lst)
    for i in range(total_rows):
        set.insert(parent='', index='end', iid=i, text='',
                   values=lst[i])

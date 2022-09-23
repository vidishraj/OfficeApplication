import tkinter as tk
from Services.CustomerServices import createCustomer


def createCustomerComponent(rootWindow: tk.Tk, frame1):
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    name = tk.StringVar()
    age = tk.IntVar()
    aadhar = tk.IntVar()
    customerType = tk.StringVar()
    customerType.set("Pick the type of Customer")
    tk.Label(frame, text='Please enter the name of the customer:').place(relx=0.2, rely=0.2, anchor='center')
    tk.Entry(frame, textvariable=name).place(relx=0.5, rely=0.2, anchor='center')
    tk.Label(frame, text='Please enter the age of the customer').place(relx=0.2, rely=0.3, anchor='center')
    tk.Entry(frame, textvariable=age).place(relx=0.5, rely=0.3, anchor='center')
    tk.Label(frame, text='Please enter the aadhar of the customer:').place(relx=0.2, rely=0.4, anchor='center')
    tk.Entry(frame, textvariable=aadhar).place(relx=0.5, rely=0.4, anchor='center')
    tk.Label(frame, text='Please choose the type of customer:').place(relx=0.2, rely=0.5, anchor='center')
    customerTypeList=('Retail','Non-Retail')
    customerMenu = tk.OptionMenu(frame, customerType, *customerTypeList)
    customerMenu.place(relx=0.5, rely=0.5, anchor='center')
    tk.Button(frame, text="Confirm",
              command=lambda:[createCustomer(name.get(), age.get(), aadhar.get(), customerType.get()),frame.destroy()]).place(relx=0.2, rely=0.65, anchor='center')
    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

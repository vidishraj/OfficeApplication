import tkinter as tk
from Services.CustomerServices import CustomerService


class UserCustomerGUI:
    _rootWindow: tk.Tk
    _parentFrame: tk.Frame
    _CustomerService: CustomerService

    def __init__(self, rootWindow, Frame, userData):
        self._rootWindow = rootWindow
        self._parentFrame = Frame
        self._CustomerService = CustomerService(userData)

    def createCustomerComponent(self):
        frame = tk.Frame(self._rootWindow, width=800, height=800)
        frame.grid(row=0, column=0, sticky='news')
        frame.tkraise(self._parentFrame)
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
        customerTypeList = ('Retail', 'Non-Retail')
        customerMenu = tk.OptionMenu(frame, customerType, *customerTypeList)
        customerMenu.place(relx=0.5, rely=0.5, anchor='center')
        tk.Button(frame, text="Confirm",
                  command=lambda: [
                      self._CustomerService.createCustomer(name.get(), age.get(), aadhar.get(), customerType.get()),
                      frame.destroy()]).place(relx=0.2, rely=0.65, anchor='center')
        tk.Button(frame, text="Back",
                  command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

    def ListCustomer(self):
        frame = tk.Frame(self._rootWindow, width=800, height=800)
        frame.grid(row=0, column=0, sticky='news')
        frame.tkraise(self._parentFrame)
        table = tk.ttk.Treeview(frame)
        table.place(relx=0.5, rely=0.25, anchor='center')
        table['columns'] = ('Name', 'Age', 'Aadhar', "Type", "Account Number")
        table.column("#0", width=0, stretch="no")
        table.column("Name", anchor="center", width=150)
        table.column("Age", anchor="center", width=50)
        table.column("Aadhar", anchor="center", width=150)
        table.column("Type", anchor="center", width=80)
        table.column("Account Number", anchor="center", width=150)

        table.heading("#0", text="", anchor="center")
        table.heading("Name", text="Name", anchor="center")
        table.heading("Age", text="Age", anchor="center")
        table.heading("Aadhar", text="Aadhar ", anchor="center")
        table.heading("Type", text="Type", anchor="center")
        table.heading("Account Number", text="Account Number", anchor="center")

        tk.Button(frame, text="Back",
                  command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
        customerList = self._CustomerService.returnCustomerList()

        total_rows = len(customerList)
        for i in range(total_rows):
            table.insert(parent='', index='end', iid=i, text='',
                         values=customerList[i])

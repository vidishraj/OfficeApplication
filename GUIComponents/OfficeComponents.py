import tkinter as tk
from Services.OfficeServices import OfficeService


class UserOfficeGUI:
    _rootWindow: tk.Tk
    _parentFrame: tk.Frame
    _OfficeService: OfficeService

    def __init__(self, rootWindow, Frame, userData):
        self._rootWindow = rootWindow
        self._parentFrame = Frame
        self._OfficeService = OfficeService(userData)

    def addOfficeOption(self):
        try:
            frame = tk.Frame(self._rootWindow, width=800, height=800)
            frame.grid(row=0, column=0, sticky='news')
            frame.tkraise(self._parentFrame)
            tk.Label(frame, text='What type of office would you like to add?').place(relx=0.5, rely=0.2,
                                                                                     anchor='center')
            tk.Button(frame, text='International Office',
                      command=lambda: self.renderMenuForOffice(frame, True), fg='black',
                      bg='white').place(relx=0.4, rely=0.3,
                                        anchor='center')
            tk.Button(frame, text='Local Office', command=lambda: self.renderMenuForOffice(frame, False),
                      fg='black',
                      bg='white').place(relx=0.6, rely=0.3,
                                        anchor='center')
        except Exception as E:
            print(E)

    def renderMenuForOffice(self, frame, choice):
        name = tk.StringVar()
        location = tk.StringVar()
        employeeCount = tk.IntVar()
        tk.Label(frame, text='Enter the name of the office:').place(relx=0.2, rely=0.4, anchor='center')
        tk.Entry(frame, textvariable=name).place(relx=0.5, rely=0.4, anchor='center')
        tk.Label(frame, text='Enter the location of the office:').place(relx=0.2, rely=0.5, anchor='center')
        tk.Entry(frame, textvariable=location).place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(frame, text='Enter the number of employees in the office:').place(relx=0.2, rely=0.65, anchor='center')
        tk.Entry(frame, textvariable=employeeCount).place(relx=0.5, rely=0.65, anchor='center')
        tk.Button(frame, text="Confirm data",
                  command=lambda: [self._OfficeService.addOffice(name.get(), location.get(), True,
                                                                 employeeCount.get()) if choice else
                                   self._OfficeService.addOffice(name.get(), location.get(), False, employeeCount.get())
                      , frame.destroy()]).place(
            relx=0.2, rely=0.7,
            anchor='center')
        tk.Button(frame, text="Back",
                  command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

    def listOffices(self):
        try:
            frame = tk.Frame(self._rootWindow, width=800, height=800)
            frame.grid(row=0, column=0, sticky='news')
            frame.tkraise(self._parentFrame)
            table = tk.ttk.Treeview(frame)
            table.place(relx=0.5, rely=0.25, anchor='center')
            table['columns'] = ('Name', 'Location', 'Type', "Employee Count", "Expenses", "Limit")
            table.column("#0", width=0, stretch="no")
            table.column("Name", anchor="center", width=150)
            table.column("Location", anchor="center", width=150)
            table.column("Type", anchor="center", width=150)
            table.column("Employee Count", anchor="center", width=150)
            table.column("Expenses", anchor="center", width=50)
            table.column("Limit", anchor="center", width=150)

            table.heading("#0", text="", anchor="center")
            table.heading("Name", text="Name", anchor="center")
            table.heading("Location", text="Location", anchor="center")
            table.heading("Type", text="Type", anchor="center")
            table.heading("Employee Count", text="Employee Count", anchor="center")
            table.heading("Expenses", text="Expenses", anchor="center")
            table.heading("Limit", text="Limit", anchor="center")

            tk.Button(frame, text="Back",
                      command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
            userOfficeInfo = self._OfficeService.listOffices()
            for i in range(len(userOfficeInfo)):
                table.insert(parent='', index='end', iid=i, text='',
                             values=userOfficeInfo[i])
        except Exception as E:
            print(E)

    def addExpenseOption(self):
        frame = tk.Frame(self._rootWindow, width=800, height=800)
        frame.grid(row=0, column=0, sticky='news')
        frame.tkraise(self._parentFrame)
        newExpense = tk.IntVar(frame)
        officeName = tk.StringVar(frame)
        officeNameList=self._OfficeService.returnOfficeNames()
        officeName.set("Choose Office")
        tk.Label(frame, text='Pick the office you want to add an expense for:').place(relx=0.5, rely=0.2,
                                                                                      anchor='center')
        officeMenu = tk.OptionMenu(frame, officeName, *officeNameList)
        officeMenu.place(relx=0.5, rely=0.3, anchor='center')
        tk.Button(frame, text="Confirm data",
                  command=lambda: [addExpense()]).place(
            relx=0.2, rely=0.7,
            anchor='center')

        def addExpense():
            tk.Label(frame, text='Enter the expense to add:').place(relx=0.2, rely=0.4,
                                                                    anchor='center')
            tk.Entry(frame, textvariable=newExpense).place(relx=0.4, rely=0.4, anchor='center')
            tk.Button(frame, text="Confirm data",
                      command=lambda: [self._OfficeService.setExpense(officeName.get,newExpense.get()), frame.destroy()]).place(
                relx=0.2, rely=0.7,
                anchor='center')

        tk.Button(frame, text="Back",
                  command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

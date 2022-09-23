import tkinter as tk
from Classes.OfficeClass import Office
from Services.OfficeServices import addOffice, OfficeList


def addOfficeOption(rootWindow: tk.Tk, frame1):
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    tk.Label(frame, text='What type of office would you like to add?').place(relx=0.5, rely=0.2, anchor='center')
    tk.Button(frame, text='International Office',
              command=lambda: renderMenuForOffice(rootWindow, frame, True), fg='black',
              bg='white').place(relx=0.4, rely=0.3,
                                anchor='center')
    tk.Button(frame, text='Local Office', command=lambda: renderMenuForOffice(rootWindow, frame, False),
              fg='black',
              bg='white').place(relx=0.6, rely=0.3,
                                anchor='center')


def addExpenseOption(rootWindow, frame1):
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    nameToObjectdict = {}
    for Office in OfficeList:
        nameToObjectdict[Office.getName()] = Office
    newExpense = tk.IntVar(frame)
    value_inside = tk.StringVar(frame)
    value_inside.set("Choose Office")
    tk.Label(frame, text='Pick the office you want to add an expense for:').place(relx=0.5, rely=0.2, anchor='center')
    officeMenu = tk.OptionMenu(frame, value_inside, *[office.getName() for office in OfficeList])
    officeMenu.place(relx=0.5, rely=0.3, anchor='center')
    tk.Button(frame, text="Confirm data",
              command=lambda:[addExpense()]).place(
        relx=0.2, rely=0.7,
        anchor='center')
    def addExpense():
        tk.Label(frame, text='Enter the expense to add:').place(relx=0.2, rely=0.4,
                                                                                   anchor='center')
        tk.Entry(frame, textvariable=newExpense).place(relx=0.4, rely=0.4, anchor='center')
        selectedOffice: Office = nameToObjectdict[value_inside.get()]
        tk.Button(frame, text="Confirm data",
                 command=lambda: [ selectedOffice.addExpense(newExpense.get()),frame.destroy()]).place(
            relx=0.2, rely=0.7,
            anchor='center')
    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')


def renderMenuForOffice(rootWindow, frame, choice):
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
              command=lambda: [addOffice(name.get(), location.get(), True,
                                         employeeCount.get()) if choice else addOffice(name.get(),
                                                                                       location.get(), False,
                                                                                       employeeCount.get()),
                               frame.destroy()]).place(
        relx=0.2, rely=0.7,
        anchor='center')
    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

from Classes.OfficeClass import Office
import tkinter as tk

OfficeList = []


def addOffice(name, location, officeType, employeeCount):
    try:
        newOffice = Office(name, location, officeType, employeeCount)
        OfficeList.append(newOffice)
    except Exception as e:
        print(e)


def listOffices(rootWindow: tk.Tk, frame1):
    lst = []
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
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
    for office in OfficeList:
        temp = [office.getName(), office.getLocation(), office.getTypeString(), office.getEmployeeCount(),
                office.getExpense(), 2000000]
        lst.append(temp)

    total_rows = len(lst)
    for i in range(total_rows):
        table.insert(parent='', index='end', iid=i, text='',
                     values=lst[i])

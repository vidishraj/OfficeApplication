import tkinter as tk
from Services import EmployeeServices
from tkcalendar import Calendar

def setManager(rootWindow: tk.Tk , frame1):
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    if len(EmployeeServices.EmployeeList) > 0:
        tk.Label(frame, text='Please choose the Employee:').place(relx=0.2, rely=0.2, anchor='center')
        employeeValue = tk.StringVar(frame)
        employeeValue.set("Choose Employee")
        employeeNameList = []
        nameToObjectdict = {}
        for Employee in EmployeeServices.EmployeeList:
            nameToObjectdict[Employee.getName()] = Employee
            employeeNameList.append(Employee.getName())
        employee_menu = tk.OptionMenu(frame, employeeValue, *employeeNameList)
        employee_menu.place(relx=0.5, rely=0.2, anchor='center')
        tk.Label(frame, text='Please choose the Manager:').place(relx=0.2, rely=0.4, anchor='center')
        managerValue = tk.StringVar(frame)
        managerValue.set("Choose Manager:")
        managerNameList = []
        managerNameToObjectdict = {}
        for Manager in EmployeeServices.ManagerList:
            managerNameToObjectdict[Manager.getName()] = Manager
            managerNameList.append(Manager.getName())
        managerMenu = tk.OptionMenu(frame, managerValue, *managerNameList)
        managerMenu.place(relx=0.5, rely=0.4, anchor='center')
        tk.Button(frame, text="Submit",
                  command=lambda :confirmChoice(), fg='black',
                  bg='white').place(
            relx=0.2, rely=0.7,
            anchor='center')
        def confirmChoice():
            #frame.destroy()
            newFrame = tk.Frame(rootWindow, width=800, height=800)
            newFrame.grid(row=0, column=0, sticky='news')
            newFrame.tkraise(frame)
            tk.Label(newFrame, text=f"Set {managerNameToObjectdict[managerValue.get()].getName()} as {nameToObjectdict[employeeValue.get()].getName()}'s manager?").place(relx=0.2, rely=0.4, anchor='center')
            tk.Button(newFrame, text="Confirm",
                      command=lambda :[nameToObjectdict[employeeValue.get()].addManager(managerNameToObjectdict[managerValue.get()]),newFrame.destroy(),frame.destroy()]).place(relx=0.1, rely=0.5, anchor='center')
            tk.Button(newFrame, text="Back",
                      command=newFrame.destroy).place(relx=0.4, rely=0.5, anchor='center')

    else:
        tk.Label(frame, text='There are no employees currently.').place(relx=0.2, rely=0.2, anchor='center')
    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

def renderMenuforEmployee(rootWindow: tk.Tk, frame, choice):
    name = tk.StringVar()
    age = tk.StringVar()
    tk.Label(frame, text='Enter the name of the employee:').place(relx=0.2, rely=0.4, anchor='center')
    tk.Entry(frame, textvariable=name).place(relx=0.5, rely=0.4, anchor='center')
    tk.Label(frame, text='Enter the age of the employee:').place(relx=0.2, rely=0.5, anchor='center')
    tk.Entry(frame, textvariable=age).place(relx=0.5, rely=0.5, anchor='center')
    tk.Label(frame, text='Select the date of joining of the employee:').place(relx=0.2, rely=0.65, anchor='center')
    cal = Calendar(frame, font="Arial 6", selectmode='day',
                   year=2022, month=5,
                   day=22)
    cal.place(relx=0.5, rely=0.65, anchor='center')
    tk.Button(frame, text="Confirm data",
              command=lambda: EmployeeServices.insertEmployee(name.get(), age.get(), cal.get_date(), choice,
                                                              frame.destroy())).place(
        relx=0.2, rely=0.7,
        anchor='center')
    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')


def renderChangePage(rootWindow: tk.Tk, frame1, choice):
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    if len(EmployeeServices.EmployeeList) > 0:
        tk.Label(frame, text='Please choose the Employee:').place(relx=0.2, rely=0.2, anchor='center')
        value_inside = tk.StringVar(frame)
        value_inside.set("Choose Employee")
        employeeNameList = []
        nameToObjectdict = {}
        for Employee in EmployeeServices.EmployeeList:
            nameToObjectdict[Employee.getName()] = Employee
            employeeNameList.append(Employee.getName())
        employee_menu = tk.OptionMenu(frame, value_inside, *employeeNameList)
        employee_menu.place(relx=0.5, rely=0.2, anchor='center')
        tk.Button(frame, text="Confirm",
                  command=lambda: EmployeeServices.changeSalary(nameToObjectdict[value_inside.get()],
                                                                frame) if choice == "salary" else EmployeeServices.changeWorktime(
                      nameToObjectdict[value_inside.get()], frame), fg='black',
                  bg='white').place(
            relx=0.2, rely=0.7,
            anchor='center')
    else:
        tk.Label(frame, text='There are no employees currently.').place(relx=0.2, rely=0.2, anchor='center')
    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')


def addEmployeeOption(rootWindow: tk.Tk, frame1):
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    employeeType = tk.StringVar()
    tk.Label(frame, text='What type of employee would you like to add?').place(relx=0.5, rely=0.2, anchor='center')
    tk.Button(frame, text='Software Engineer',
              command=lambda: renderMenuforEmployee(rootWindow, frame, "createSoftEngineer"), fg='black',
              bg='white').place(relx=0.1, rely=0.3,
                                anchor='center')
    tk.Button(frame, text='Manager', command=lambda: renderMenuforEmployee(rootWindow, frame, "createManager"),
              fg='black',
              bg='white').place(relx=0.3, rely=0.3,
                                anchor='center')
    tk.Button(frame, text='Architect', command=lambda: renderMenuforEmployee(rootWindow, frame, "createArchitect"),
              fg='black',
              bg='white').place(relx=0.5, rely=0.3,
                                anchor='center')
    tk.Button(frame, text='Maids', command=lambda: renderMenuforEmployee(rootWindow, frame, "createMaid"),
              fg='black',
              bg='white').place(relx=0.7, rely=0.3,
                                anchor='center')
    tk.Button(frame, text='IT Staff', command=lambda: renderMenuforEmployee(rootWindow, frame, "createITStaff"),
              fg='black',
              bg='white').place(relx=0.9, rely=0.3,
                                anchor='center')

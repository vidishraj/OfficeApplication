import tkinter as tk
from Classes import EmployeeSubclasses
from Classes import EmployeeClass

EmployeeList: list = []
ManagerList: list = []


def insertEmployee(name, age, dateOfJoining, choice, frameDestroyCommand):
    if choice == "createMaid":
        newemp = EmployeeSubclasses.Maid(name, age, dateOfJoining)
    elif choice == "createSoftEngineer":
        newemp = EmployeeSubclasses.SoftwareEngineer(name, age, dateOfJoining)
    elif choice == "createArchitect":
        newemp = EmployeeSubclasses.Architect(name, age, dateOfJoining)
    elif choice == "createManager":
        newemp = EmployeeClass.Manager(name, age, dateOfJoining)
        ManagerList.append(newemp)
    elif choice == "createITStaff":
        newemp = EmployeeSubclasses.ITstaff(name, age, dateOfJoining)
    EmployeeList.append(newemp)
    return newemp

def changeSalary(Employee, frame):
    tk.Label(frame, text='Enter the new salary of the employee:').place(relx=0.2, rely=0.4,
                                                                              anchor='center')
    new_salary = tk.IntVar(frame,0)
    tk.Entry(frame, textvariable=new_salary).place(relx=0.4, rely=0.4, anchor='center')
    tk.Button(frame, text="Confirm",
              command=lambda: [Employee.setSalary(new_salary.get()) , frame.destroy()], fg='black',
              bg='white').place(
        relx=0.2, rely=0.7,
        anchor='center')



def changeWorktime(Employee, frame):
    tk.Label(frame, text='Enter the new working hours of the employee:').place(relx=0.2, rely=0.4,
                                                                        anchor='center')
    newWorkingHours= tk.IntVar(frame,0)
    tk.Entry(frame, textvariable=newWorkingHours).place(relx=0.4, rely=0.4, anchor='center')
    tk.Button(frame, text="Confirm",
              command=lambda: [Employee.setWorkingHours(newWorkingHours.get()), frame.destroy()], fg='black',
              bg='white').place(
        relx=0.2, rely=0.7,
        anchor='center')


def listEmployees(rootWindow: tk.Tk, frame1):
    lst = []
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise(frame1)
    set = tk.ttk.Treeview(frame)
    set.place(relx=0.5, rely=0.25, anchor='center')
    set['columns'] = ('Name', 'Salary', 'Working Hours', "Manager", "Age", "DOJ")
    set.column("#0", width=0, stretch="no")
    set.column("Name", anchor="center", width=150)
    set.column("Salary", anchor="center", width=150)
    set.column("Working Hours", anchor="center", width=150)
    set.column("Manager", anchor="center", width=150)
    set.column("Age", anchor="center", width=50)
    set.column("DOJ", anchor="center", width=150)

    set.heading("#0", text="", anchor="center")
    set.heading("Name", text="Name", anchor="center")
    set.heading("Salary", text="Salary", anchor="center")
    set.heading("Working Hours", text="Working Hours", anchor="center")
    set.heading("Manager", text="Manager", anchor="center")
    set.heading("Age", text="Age", anchor="center")
    set.heading("DOJ", text="Date of Joining", anchor="center")

    tk.Button(frame, text="Back",
              command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
    for Employee in EmployeeList:
        managerName = ""
        if Employee.getManager() is not None:
            managerName = Employee.getManager().getName()

        temp = [Employee.getName(), Employee.getSalary(), Employee.getWorkingHours(), managerName, Employee.getAge(),
                Employee.getDOJ()]
        lst.append(temp)

    total_rows = len(lst)
    for i in range(total_rows):
        set.insert(parent='', index='end', iid=i, text='',
                   values=lst[i])

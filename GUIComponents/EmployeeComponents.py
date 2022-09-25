import tkinter as tk
from Services.EmployeeServices import EmployeeService
from tkcalendar import Calendar


class UserEmployeeGUI:
    _rootWindow: tk.Tk
    _parentFrame: tk.Frame
    _EmployeeService: EmployeeService

    def __init__(self, rootWindow, Frame, userData):
        self._rootWindow = rootWindow
        self._parentFrame = Frame
        self._EmployeeService = EmployeeService(userData)

    def employeeChoiceMenu(self):
        try:
            frame = tk.Frame(self._rootWindow, width=800, height=800)
            frame.grid(row=0, column=0, sticky='news')
            frame.tkraise(self._parentFrame)
            tk.Label(frame, text='What type of employee would you like to add?').place(relx=0.5, rely=0.2,
                                                                                       anchor='center')
            tk.Button(frame, text='Software Engineer',
                      command=lambda: self.employeeDetailsEntryMenu(frame, "createSoftwareEngineer"),
                      fg='black',
                      bg='white').place(relx=0.1, rely=0.3,
                                        anchor='center')
            tk.Button(frame, text='Manager',
                      command=lambda: self.employeeDetailsEntryMenu(frame, "createManager"),
                      fg='black',
                      bg='white').place(relx=0.3, rely=0.3,
                                        anchor='center')
            tk.Button(frame, text='Architect',
                      command=lambda: self.employeeDetailsEntryMenu(frame, "createArchitect"),
                      fg='black',
                      bg='white').place(relx=0.5, rely=0.3,
                                        anchor='center')
            tk.Button(frame, text='Maids',
                      command=lambda: self.employeeDetailsEntryMenu(frame, "createMaid"),
                      fg='black',
                      bg='white').place(relx=0.7, rely=0.3,
                                        anchor='center')
            tk.Button(frame, text='IT Staff',
                      command=lambda: self.employeeDetailsEntryMenu(frame, "createITStaff"),
                      fg='black',
                      bg='white').place(relx=0.9, rely=0.3,
                                        anchor='center')
        except Exception as E:
            print(E)

    def employeeDetailsEntryMenu(self, frame, choice):
        try:
            name = tk.StringVar()
            age = tk.StringVar()
            tk.Label(frame, text='Enter the name of the employee:').place(relx=0.2, rely=0.4,
                                                                          anchor='center')
            tk.Entry(frame, textvariable=name).place(relx=0.5, rely=0.4, anchor='center')
            tk.Label(frame, text='Enter the age of the employee:').place(relx=0.2, rely=0.5,
                                                                         anchor='center')
            tk.Entry(frame, textvariable=age).place(relx=0.5, rely=0.5, anchor='center')
            tk.Label(frame, text='Select the date of joining of the employee:').place(relx=0.2, rely=0.65,
                                                                                      anchor='center')
            cal = Calendar(frame, font="Arial 6", selectmode='day',
                           year=2022, month=5,
                           day=22)
            cal.place(relx=0.5, rely=0.65, anchor='center')
            tk.Button(frame, text="Confirm data",
                      command=lambda: [
                          self._EmployeeService.insertEmployee(name.get(), age.get(), cal.get_date(), choice,
                                                               ), frame.destroy()]).place(
                relx=0.2, rely=0.7,
                anchor='center')
            tk.Button(frame, text="Back",
                      command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')
        except Exception as E:
            print(E)

    def listEmployees(self):
        try:
            frame = tk.Frame(self._rootWindow, width=800, height=800)
            frame.grid(row=0, column=0, sticky='news')
            frame.tkraise(self._parentFrame)
            table = tk.ttk.Treeview(frame)
            table.place(relx=0.5, rely=0.25, anchor='center')
            table['columns'] = ('Name', 'Salary', 'Working Hours', "Manager", "Age", "DOJ")
            table.column("#0", width=0, stretch="no")
            table.column("Name", anchor="center", width=150)
            table.column("Salary", anchor="center", width=150)
            table.column("Working Hours", anchor="center", width=150)
            table.column("Manager", anchor="center", width=150)
            table.column("Age", anchor="center", width=50)
            table.column("DOJ", anchor="center", width=150)

            table.heading("#0", text="", anchor="center")
            table.heading("Name", text="Name", anchor="center")
            table.heading("Salary", text="Salary", anchor="center")
            table.heading("Working Hours", text="Working Hours", anchor="center")
            table.heading("Manager", text="Manager", anchor="center")
            table.heading("Age", text="Age", anchor="center")
            table.heading("DOJ", text="Date of Joining", anchor="center")

            tk.Button(frame, text="Back",
                      command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
            employeeList = self._EmployeeService.returnEmployeeList()
            for i in range(len(employeeList)):
                table.insert(parent='', index='end', iid=i, text='',
                             values=employeeList[i])
        except Exception as E:
            print(E)

    def setManager(self):
        frame = tk.Frame(self._parentFrame, width=800, height=800)
        frame.grid(row=0, column=0, sticky='news')
        frame.tkraise(self._parentFrame)
        if len(self._EmployeeService.returnEmployeeList()) > 0:
            tk.Label(frame, text='Please choose the Employee:').place(relx=0.2, rely=0.2, anchor='center')
            employeeValue = tk.StringVar(frame)
            employeeValue.set("Choose Employee")
            employeeNameList = self._EmployeeService.returnEmployeeNameList()
            employee_menu = tk.OptionMenu(frame, employeeValue, *employeeNameList)
            employee_menu.place(relx=0.5, rely=0.2, anchor='center')
            tk.Label(frame, text='Please choose the Manager:').place(relx=0.2, rely=0.4, anchor='center')
            managerValue = tk.StringVar(frame)
            managerValue.set("Choose Manager:")
            managerNameList = self._EmployeeService.returnManagerNameList()
            managerMenu = tk.OptionMenu(frame, managerValue, *managerNameList)
            managerMenu.place(relx=0.5, rely=0.4, anchor='center')
            tk.Button(frame, text="Submit",
                      command=lambda: confirmChoice(), fg='black',
                      bg='white').place(
                relx=0.2, rely=0.7,
                anchor='center')
        else:
            tk.Label(frame, text='There are no employees currently.').place(relx=0.2, rely=0.2, anchor='center')
        tk.Button(frame, text="Back",
                  command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

        def confirmChoice():
            newFrame = tk.Frame(self._rootWindow, width=800, height=800)
            newFrame.grid(row=0, column=0, sticky='news')
            newFrame.tkraise(frame)
            tk.Label(newFrame,
                     text=f"table {self._EmployeeService.returnManagerFromName(managerValue.get()).getName()} as "
                          f"{self._EmployeeService.returnEmployeeFromName(employeeValue.get()).getName()}'s manager?")\
                .place(relx=0.2, rely=0.4, anchor='center')
            tk.Button(newFrame, text="Confirm",
                      command=lambda: [
                          self._EmployeeService.returnEmployeeFromName(employeeValue.get()).addManager(
                              self._EmployeeService.returnManagerFromName(managerValue.get())),
                          newFrame.destroy(), frame.destroy()]).place(relx=0.1, rely=0.5, anchor='center')
            tk.Button(newFrame, text="Back",
                      command=newFrame.destroy).place(relx=0.4, rely=0.5, anchor='center')

    def renderChangePage(self, choice):
        frame = tk.Frame(self._rootWindow, width=800, height=800)
        frame.grid(row=0, column=0, sticky='news')
        frame.tkraise(self._parentFrame)
        if len(self._EmployeeService.returnEmployeeList()) > 0:
            tk.Label(frame, text='Please choose the Employee:').place(relx=0.2, rely=0.2, anchor='center')
            employeeName = tk.StringVar(frame)
            employeeName.set("Choose Employee")
            employeeNameList = self._EmployeeService.returnEmployeeNameList()
            employee_menu = tk.OptionMenu(frame, employeeName, *employeeNameList)
            employee_menu.place(relx=0.5, rely=0.2, anchor='center')
            tk.Button(frame, text="Confirm",
                      command=lambda: setSalary() if choice == "salary" else setWorkTime(), fg='black',
                      bg='white').place(
                relx=0.2, rely=0.7,
                anchor='center')
        else:
            tk.Label(frame, text='There are no employees currently.').place(relx=0.2, rely=0.2, anchor='center')
        tk.Button(frame, text="Back",
                  command=frame.destroy).place(relx=0.2, rely=0.75, anchor='center')

        def setSalary():
            tk.Label(frame, text='Enter the new salary of the employee:').place(relx=0.2, rely=0.4,
                                                                                anchor='center')
            newSalary = tk.IntVar(frame, 0)
            tk.Entry(frame, textvariable=newSalary).place(relx=0.4, rely=0.4, anchor='center')
            tk.Button(frame, text="Confirm",
                      command=lambda: [self._EmployeeService.changeSalary(employeeName.get(), newSalary.get()),
                                       frame.destroy()], fg='black',
                      bg='white').place(
                relx=0.2, rely=0.7,
                anchor='center')

        def setWorkTime():
            tk.Label(frame, text='Enter the new working hours of the employee:').place(relx=0.2, rely=0.4,
                                                                                       anchor='center')
            newWorkingHours = tk.IntVar(frame, 0)
            tk.Entry(frame, textvariable=newWorkingHours).place(relx=0.4, rely=0.4, anchor='center')
            tk.Button(frame, text="Confirm",
                      command=lambda: [self._EmployeeService.changeWorktime(employeeName.get(), newWorkingHours.get()),
                                       frame.destroy()], fg='black',
                      bg='white').place(
                relx=0.2, rely=0.7,
                anchor='center')

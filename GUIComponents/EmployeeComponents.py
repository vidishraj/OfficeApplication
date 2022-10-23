import tkinter as tk
from tkinter import ttk
import customtkinter
import tkcalendar
from PIL import Image, ImageTk

from Services.EmployeeServices import EmployeeService
from tkcalendar import Calendar, DateEntry


class UserEmployeeGUI:
    _rootWindow: customtkinter.CTk
    _parentFrame: customtkinter.CTkFrame
    _EmployeeService: EmployeeService

    def __init__(self, rootWindow, Frame, userData):
        self._rootWindow = rootWindow
        self._parentFrame = Frame
        self._EmployeeService = EmployeeService(userData)

    def employeeChoiceMenu(self):
        try:
            newWindow=customtkinter.CTkToplevel()
            newWindow.geometry(self._rootWindow.winfo_geometry())
            frame=customtkinter.CTkFrame(newWindow, width=1000, height=800)
            frame.place(relx=0, rely=0)
            frame.tkraise(self._parentFrame)
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                   text_color="black", text="What type of employee would you like to add?", width=100,
                                   corner_radius=50, height=30, compound="top").place(relx=0.25, rely=0.2,
                                                                                      anchor='center')
            AddEmployee = ImageTk.PhotoImage(Image.open("assets/addEmployee.png").resize((50, 50), Image.ANTIALIAS))
            
            AddManager = ImageTk.PhotoImage(Image.open("assets/manager.png").resize((50, 50), Image.ANTIALIAS))
            AddMaid = ImageTk.PhotoImage(Image.open("assets/maid.png").resize((50, 50), Image.ANTIALIAS))
            AddArchitect = ImageTk.PhotoImage(Image.open("assets/architect.png").resize((50, 50), Image.ANTIALIAS))
            AddITStaff = ImageTk.PhotoImage(Image.open("assets/ITstaff.png").resize((50, 50), Image.ANTIALIAS))
            exit = ImageTk.PhotoImage(Image.open("assets/exit.png").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=( "Malgun Gothic", 10),image=AddEmployee,master=frame,fg_color="white",
                                    text_color="black",text="Manager", width=80,corner_radius=50, height=70,compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame, "createSoftwareEngineer")).place(relx=0.25, rely=0.3,anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddManager, master=frame, fg_color="white",
                                    text_color="black", text="Manager", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createSoftwareEngineer")).place(
                relx=0.25, rely=0.4, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddArchitect, master=frame, fg_color="white",
                                    text_color="black", text="Architect", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createSoftwareEngineer")).place(
                relx=0.25, rely=0.5, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddITStaff, master=frame, fg_color="white",
                                    text_color="black", text="IT Staff", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createSoftwareEngineer")).place(
                relx=0.25, rely=0.6, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddMaid, master=frame, fg_color="white",
                                    text_color="black", text="Maid", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createSoftwareEngineer")).place(
                relx=0.25, rely=0.7, anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=exit, master=frame, fg_color="white",
                                    text_color="black", text="Exit", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=self._rootWindow.destroy).place(relx=0.9, rely=0.1, anchor='center')
            newWindow.mainloop()
        except Exception as E:
            print(E)

    def employeeDetailsEntryMenu(self, frame, choice):
        try:
            name = tk.StringVar()
            age = tk.StringVar()
            selectedDate = tk.StringVar(master=frame)
            selectedDate.set("Select the data:")
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                   text_color="black", text="Enter the name of the employee:", width=100,
                                   corner_radius=50, height=30, compound="top").place(relx=0.6, rely=0.3,
                                                                                      anchor='center')
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                   text_color="black", text="Enter the age of the employee:", width=100,
                                   corner_radius=50, height=30, compound="top").place(relx=0.6, rely=0.4,
                                                                                      anchor='center')
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                   text_color="black", text='Select the date of joining of the employee:', width=100,
                                   corner_radius=50, height=30, compound="top").place(relx=0.6, rely=0.5,
                                                                                      anchor='center')

            customtkinter.CTkEntry(frame, textvariable=name, border_color="white", corner_radius=5,
                                   text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.9, rely=0.3, anchor='center')

            customtkinter.CTkEntry(frame, textvariable=age, border_color="white", corner_radius=5,
                                   text_color="white", width=100, height=2, text_font=("Bold", 8)).place(relx=0.9,
                                                                                                         rely=0.4,
                                                                                                         anchor='center')
            style = ttk.Style()
            style.configure('my.DateEntry',
                            corner_radius=50,
                            width=100,
                            text_color="white",
                            fieldbackground='black',
                            background='white',
                            foreground='white',
                            arrowcolor='white')
            cal=DateEntry(master=frame,textvariable=selectedDate,style='my.DateEntry')
            cal.config(background = "black")
            cal.place(relx=0.9, rely=0.5, anchor='center')
            back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))

            confirm = ImageTk.PhotoImage(Image.open("assets/confirm.webp").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                      command= self._rootWindow.destroy).place(relx=0.65, rely=0.6, anchor='center')


            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=confirm, master=frame, fg_color="white",
                                    text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=lambda: [
                                        self._EmployeeService.insertEmployee(name.get(), age.get(), cal.get_date(),
                                                                             choice,
                                                                             ), self._rootWindow.destroy()]).place(relx=0.5, rely=0.6, anchor='center')
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

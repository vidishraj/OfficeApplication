import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk

from PopUps.ErrorPopUp import ErrorPopUp
from PopUps.ConfirmationPopUp import ConfirmationPopUp

from Services.EmployeeServices import EmployeeService
from tkcalendar import DateEntry
from logger import logging

logger = logging.getLogger('Office Application')


class UserEmployeeGUI:
    _rootWindow: customtkinter.CTk
    _parentFrame: customtkinter.CTkFrame
    _EmployeeService: EmployeeService

    def __init__(self, rootWindow, Frame, userData):
        self._rootWindow = rootWindow
        self._parentFrame = Frame
        self._EmployeeService = EmployeeService(userData)
        self.back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))
        self.confirm = ImageTk.PhotoImage(Image.open("assets/confirm.webp").resize((50, 50), Image.ANTIALIAS))

    def employeeChoiceMenu(self):
        try:
            frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
            frame.place(relx=0, rely=0)
            logger.info("Opened Employee Choice Menu.")
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                   text_color="black", text="What type of employee would you like to add?", width=100,
                                   corner_radius=50, height=30, compound="top").place(relx=0.25, rely=0.2,
                                                                                      anchor='center')
            # Icons
            AddEmployee = ImageTk.PhotoImage(Image.open("assets/addEmployee.png").resize((50, 50), Image.ANTIALIAS))

            AddManager = ImageTk.PhotoImage(Image.open("assets/manager.png").resize((50, 50), Image.ANTIALIAS))
            AddMaid = ImageTk.PhotoImage(Image.open("assets/maid.png").resize((50, 50), Image.ANTIALIAS))
            AddArchitect = ImageTk.PhotoImage(Image.open("assets/architect.png").resize((50, 50), Image.ANTIALIAS))
            AddITStaff = ImageTk.PhotoImage(Image.open("assets/ITstaff.png").resize((50, 50), Image.ANTIALIAS))
            exitIcon = ImageTk.PhotoImage(Image.open("assets/exit.png").resize((50, 50), Image.ANTIALIAS))

            # Buttons
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddEmployee, master=frame, fg_color="white",
                                    text_color="black", text="Software Engineer", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createSoftwareEngineer")).place(
                relx=0.25, rely=0.3, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddManager, master=frame, fg_color="white",
                                    text_color="black", text="Manager", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createManager")).place(
                relx=0.25, rely=0.4, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddArchitect, master=frame, fg_color="white",
                                    text_color="black", text="Architect", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createArchitect")).place(
                relx=0.25, rely=0.5, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddITStaff, master=frame, fg_color="white",
                                    text_color="black", text="IT Staff", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createITStaff")).place(
                relx=0.25, rely=0.6, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=AddMaid, master=frame, fg_color="white",
                                    text_color="black", text="Maid", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.employeeDetailsEntryMenu(frame,
                                                                                  "createMaid")).place(
                relx=0.25, rely=0.7, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.7, rely=0.1, anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=exitIcon, master=frame, fg_color="white",
                                    text_color="black", text="Exit", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=self._rootWindow.destroy).place(relx=0.9, rely=0.1, anchor='center')

        except Exception as E:
            logger.error(f"Error while opening Employee Menu {E}.")

    def employeeDetailsEntryMenu(self, frame, choice):
        try:
            logger.info("Opened employee creation window.")
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
                                   text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.9,
                                   rely=0.3, anchor='center')

            customtkinter.CTkEntry(frame, textvariable=age, border_color="white", corner_radius=5,
                                   text_color="white", width=100, height=2, text_font=("Bold", 8)).place(relx=0.9,
                                   rely=0.4, anchor='center')
            style = ttk.Style()
            style.configure('my.DateEntry',
                            corner_radius=50,
                            width=100,
                            text_color="white",
                            fieldbackground='black',
                            background='white',
                            foreground='white',
                            arrowcolor='white')
            cal = DateEntry(master=frame, textvariable=selectedDate, style='my.DateEntry')
            cal.config(background="black")
            cal.place(relx=0.9, rely=0.5, anchor='center')
            back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))
            employeeCreatedPopUp = ConfirmationPopUp()
            confirm = ImageTk.PhotoImage(Image.open("assets/confirm.webp").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.65, rely=0.6, anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=confirm, master=frame, fg_color="white",
                                    text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                    compound="top", command=lambda: [self._EmployeeService.insertEmployee(name.get(),
                                                                                                          age.get(),
                                                                                                          cal.get_date(),
                                                                                                          choice, ),
                                                                     frame.destroy(),
                                                                     employeeCreatedPopUp.createConfirmationPopUp(
                                                                         "Employee Created.")]).place(relx=0.5,
                                                                                                      rely=0.6,
                                                                                                      anchor='center')
        except Exception as E:
            logger.error(f"{E}")

    def listEmployees(self):
        try:
            frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
            frame.grid(row=0, column=0, sticky='news')
            logger.info("Listing Employees.")
            style = ttk.Style()

            style.theme_use("default")

            style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
            style.map('Treeview', background=[('selected', '#22559b')])

            style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
            style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
            table = tk.ttk.Treeview(frame)
            table.place(relx=0.5, rely=0.25, anchor='center')
            table['columns'] = ('Name', 'Salary', 'Working Hours', "Manager", "Age", "DOJ")
            table.column("#0", width=0, stretch="no")
            table.column("Name", anchor="center", width=200)
            table.column("Salary", anchor="center", width=200)
            table.column("Working Hours", anchor="center", width=200)
            table.column("Manager", anchor="center", width=200)
            table.column("Age", anchor="center", width=100)
            table.column("DOJ", anchor="center", width=200)

            table.heading("#0", text="", anchor="center")
            table.heading("Name", text="Name", anchor="center")
            table.heading("Salary", text="Salary", anchor="center")
            table.heading("Working Hours", text="Working Hours", anchor="center")
            table.heading("Manager", text="Manager", anchor="center")
            table.heading("Age", text="Age", anchor="center")
            table.heading("DOJ", text="Date of Joining", anchor="center")
            back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.5, rely=0.6, anchor='center')
            employeeList = self._EmployeeService.returnEmployeeList()
            for i in range(len(employeeList)):
                table.insert(parent='', index='end', iid=i, text='',
                             values=employeeList[i])
        except Exception as E:
            logger.error(f"Error while listing employees {E}")

    def setManager(self):
        try:
            frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
            frame.grid(row=0, column=0, sticky='news')
            logger.info("Setting Manager Menu Opened.")
            if len(self._EmployeeService.returnEmployeeList()) > 0:
                customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                       text_color="black", text="Choose Employee:", width=100,
                                       corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.2,
                                                                                          anchor='center')
                employeeValue = tk.StringVar(frame)
                employeeValue.set("Choose Employee")
                employeeNameList = self._EmployeeService.returnEmployeeNameList()
                customerMenu = customtkinter.CTkOptionMenu(frame, variable=employeeValue, values=employeeNameList,
                                                           fg_color="white", text_color="black", button_color="white")
                customerMenu.place(relx=0.5, rely=0.2, anchor='center')

                customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                       text_color="black", text="Choose Manager:", width=100,
                                       corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.4,
                                                                                          anchor='center')
                managerValue = tk.StringVar(frame)
                managerValue.set("Choose Manager:")
                managerNameList = self._EmployeeService.returnManagerNameList()
                customerMenu = customtkinter.CTkOptionMenu(frame, variable=managerValue, values=managerNameList,
                                                           fg_color="white", text_color="black", button_color="white")
                customerMenu.place(relx=0.5, rely=0.4, anchor='center')

            else:
                tk.Label(frame, text='There are no employees currently.').place(relx=0.2, rely=0.2, anchor='center')
            managerSetPopup = ConfirmationPopUp()
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.confirm, master=frame, fg_color="white",
                                    text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=lambda: [frame.destroy(),
                                                     managerSetPopup.createConfirmationPopUp("Manager set.")
                                        , self._EmployeeService.returnEmployeeFromName(employeeValue.get()).addManager(
                                            self._EmployeeService.returnManagerFromName(managerValue.get()))
                                                     ]).place(relx=0.5, rely=0.6, anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.65, rely=0.6, anchor='center')
        except Exception as ex:
            logger.error(f"Error while setting manager. {ex}")



    def renderChangePage(self, choice):
        try:
            frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
            frame.grid(row=0, column=0, sticky='news')
            if len(self._EmployeeService.returnEmployeeList()) > 0:
                customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                       text_color="black", text="Choose the Employee", width=100,
                                       corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.2,
                                                                                          anchor='center')
                employeeName = tk.StringVar(frame)
                employeeName.set("Choose Employee")
                employeeNameList = self._EmployeeService.returnEmployeeNameList()
                employeeMenu = customtkinter.CTkOptionMenu(frame, variable=employeeName, values=employeeNameList,
                                                           fg_color="white", text_color="black", button_color="white")
                employeeMenu.place(relx=0.5, rely=0.2, anchor='center')
                choose = ImageTk.PhotoImage(Image.open("assets/choose.png").resize((50, 50), Image.ANTIALIAS))
                customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=choose, master=frame, fg_color="white",
                                        text_color="black", text="Choose", width=30, corner_radius=50, height=30,
                                        compound="top", command=lambda: setSalary(frame) if choice == "salary" else
                    setWorkTime(frame)).place(relx=0.7, rely=0.2, anchor='center')
            else:
                tk.Label(frame, text='There are no employees currently.').place(relx=0.2, rely=0.2, anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.65, rely=0.6, anchor='center')
        except Exception as ex:
            logger.error(f"Error while rendering change page. {ex}")

        def setSalary(parentFrame):
            try:
                logger.info("Setting Salary.")
                customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=parentFrame, fg_color="white",
                                       text_color="black", text="Enter the new salary of the employee:", width=100,
                                       corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.4,
                                                                                          anchor='center')
                newSalary = tk.IntVar(parentFrame, 0)
                customtkinter.CTkEntry(parentFrame, textvariable=newSalary).place(relx=0.5, rely=0.4, anchor='center')
                salarySetPopUp = ConfirmationPopUp()
                customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.confirm, master=parentFrame, fg_color="white",
                                        text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                        compound="top",
                                        command=lambda: [salarySetPopUp.createConfirmationPopUp("Salary set."),
                                                         self._EmployeeService.changeWorktime(employeeName.get(),
                                                                                              newSalary.get()),
                                                         parentFrame.destroy()]).place(relx=0.5, rely=0.6, anchor='center')
            except Exception as error:
                logger.error(f"Error while setting salary. {error}")

        def setWorkTime(parentFrame):
            try:
                logger.info("Setting workhours.")
                customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=parentFrame, fg_color="white",
                                       text_color="black", text="Enter the new workhours of the employee:", width=100,
                                       corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.4,
                                                                                          anchor='center')
                newWorkingHours = tk.IntVar(parentFrame, 0)
                customtkinter.CTkEntry(parentFrame, textvariable=newWorkingHours).place(relx=0.5, rely=0.4, anchor='center')

                hoursSetPopUp = ConfirmationPopUp()
                customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.confirm, master=parentFrame, fg_color="white",
                                        text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                        compound="top",
                                        command=lambda: [hoursSetPopUp.createConfirmationPopUp("Working Hours Set."),
                                                         self._EmployeeService.changeWorktime(employeeName.get(),
                                                                                              newWorkingHours.get()),
                                                         parentFrame.destroy()]).place(relx=0.5, rely=0.6, anchor='center')
            except Exception as error:
                logger.error(f"Error while setting salary. {error}")

import json
import tkinter as tk
from tkinter import ttk

from Classes.dataHolderClass import dataHolder
from .EmployeeComponents import UserEmployeeGUI
from .CustomerComponents import UserCustomerGUI
from .AccountComponents import UserAccountGUI
from .OfficeComponents import UserOfficeGUI
import customtkinter
from PIL import Image, ImageTk
from PopUps.ErrorPopUp import ErrorPopUp
from PopUps.ConfirmationPopUp import ConfirmationPopUp

class UserInit:
    __username: str
    __password: str
    __userWindow: tk.Tk
    __userData: dataHolder

    def __init__(self):
        self.parentWindow = None
        self.userinfoFrame = None
        self.__currentUserIndex = None
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.back = None
        self.exit = None
        self.frame = None

    def initUserWindow(self):
        try:
            loginWindow = customtkinter.CTk()
            self.parentWindow = loginWindow
            loginWindow.title("OFFICE MANAGEMENT APPLICATION")
            loginWindow.geometry('450x450+400+100')
            self.userinfoFrame = customtkinter.CTkFrame(master=loginWindow, width=450, height=450, fg_color="black",
                                                        bg_color="black")
            self.userinfoFrame.place(relx=0, rely=0)
            userNameImage = ImageTk.PhotoImage(Image.open("assets/username.png").resize((75, 75), Image.ANTIALIAS))
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=self.userinfoFrame, fg_color="white",
                                   text_color="black", image=userNameImage, text="Username", width=140,
                                   corner_radius=50, height=90, compound="top").place(relx=0.5, rely=0.3,
                                                                                      anchor='center')
            userNameText = customtkinter.CTkTextbox(self.userinfoFrame, border_color="red", corner_radius=5,
                                                    text_color="white", width=100, height=2, text_font=("Bold", 8))
            userNameText.place(
                relx=0.5, rely=0.36, anchor='center')

            passwordImage = ImageTk.PhotoImage(
                Image.open("assets/password.png").resize((60, 60), Image.ANTIALIAS))
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=self.userinfoFrame, fg_color="white",
                                   text_color="black", image=passwordImage, text="Password", width=100,
                                   corner_radius=50, height=90, compound="top").place(relx=0.5, rely=0.54,
                                                                                      anchor='center')
            passwordText = customtkinter.CTkTextbox(self.userinfoFrame, border_color="red", corner_radius=5,
                                                    text_color="white", width=100, height=2, text_font=("Bold", 8))

            passwordText.place(relx=0.5, rely=0.6, anchor='center')
            customtkinter.CTkButton(self.userinfoFrame, text='Sign In', fg_color="white", text_color="black",
                                    command=lambda: [self.checkUser(userNameText.textbox.get(1.0, "end-1c"),
                                                                    passwordText.textbox.get(1.0, "end-1c"))],
                                    width=190, height=40, compound="top").place(relx=0.5, rely=0.75,
                                                                                anchor='center')
            customtkinter.CTkButton(self.userinfoFrame, text='Register', fg_color="white", text_color="black",
                                    command=lambda: [self.createUser()],
                                    width=190, height=40, compound="top").place(relx=0.5, rely=0.9,
                                                                                anchor='center')
            loginWindow.mainloop()
        except Exception as E:
            print("Problem while initialising user window." + E.__str__())

    def checkUser(self, username, email):
        try:
            self.__username = username
            self.__password = email
            CustomerFile = open('userInfo.json')
            CustomerDict = json.load(CustomerFile)
            userFlag = False
            self.__userData = dataHolder()
            for i in range(len(CustomerDict['Users'])):
                if CustomerDict['Users'][i]['Email'] == self.__username and CustomerDict['Users'][i][
                    'Password'] == self.__password:
                    userFlag = True
                    self.__userData.setCustomerList(CustomerDict['Users'][i]['CustomerList'])
                    self.__userData.setOfficeList(CustomerDict['Users'][i]['OfficeList'])
                    self.__userData.setEmployeeList(CustomerDict['Users'][i]['EmployeeList'])
                    self.__currentUserIndex = i

            if userFlag:
                self.typeChoiceWindow()
            else:
                invalidUserPopUp = ErrorPopUp("Invalid UserName or Password. Please check.", self.parentWindow)
                invalidUserPopUp.createErrorPopUp()
        except Exception as E:
            print("Problem while checking user credentials.", E)

    def createUser(self):
        try:
            registerWindow = customtkinter.CTkToplevel()
            registerWindow.geometry('450x450+400+100')
            self.userinfoFrame = customtkinter.CTkFrame(master=registerWindow, width=450, height=450, fg_color="black",
                                                        bg_color="black")

            self.userinfoFrame.place(relx=0, rely=0)
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=self.userinfoFrame, fg_color="white",
                                   text_color="black",text="Enter a valid username:", width=140,
                                   corner_radius=50, height=90, compound="top").place(relx=0.5, rely=0.2,
                                                                                      anchor='center')
            userNameText = customtkinter.CTkTextbox(self.userinfoFrame, border_color="red", corner_radius=5,
                                                    text_color="white", width=100, height=2, text_font=("Bold", 8))
            userNameText.place(
                relx=0.5, rely=0.36, anchor='center')

            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=self.userinfoFrame, fg_color="white",
                                   text_color="black", text="Enter your password:", width=100,
                                   corner_radius=50, height=90, compound="top").place(relx=0.5, rely=0.54,
                                                                                      anchor='center')
            passwordText = customtkinter.CTkTextbox(self.userinfoFrame, border_color="red", corner_radius=5,
                                                    text_color="white", width=100, height=2, text_font=("Bold", 8))

            passwordText.place(relx=0.5, rely=0.7, anchor='center')

            confirm = ImageTk.PhotoImage(Image.open("assets/confirm.webp").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=confirm, master=registerWindow, fg_color="white",
                                    text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=lambda:[addUsertoJson(),registerWindow.destroy()]).place(relx=0.5,rely=0.9,anchor='center')
            def addUsertoJson():
                CustomerFile = open('userInfo.json')
                CustomerDict = json.load(CustomerFile)
                newUser = dict()
                newUser['Email'] = userNameText.textbox.get(1.0, "end-1c")
                newUser['Password'] = passwordText.textbox.get(1.0, "end-1c")
                newUser['CustomerList'] = None
                newUser['ManagerList'] = None
                newUser['OfficeList'] = None
                newUser['EmployeeList'] = None
                CustomerDict['Users'].append(newUser)
                with open('userInfo.json', 'w', encoding='utf-8') as f:
                    json.dump(CustomerDict, f, ensure_ascii=False, indent=4)

        except Exception as e:
            print(e)
            print("Problem while creating a new user.", e)
    def typeChoiceWindow(self):
        try:
            menuWindow = self.parentWindow
            self.parentWindow = menuWindow
            menuWindow.title("OFFICE MANAGEMENT APPLICATION")
            style = ttk.Style()
            style.theme_use('clam')
            menuWindow.geometry('1000x750+300+000')
            EmployeeIcon = ImageTk.PhotoImage(Image.open("assets/employee.jpg").resize((200, 200), Image.ANTIALIAS))
            CustomerIcon = ImageTk.PhotoImage(Image.open("assets/employeeL.jpg").resize((200, 200), Image.ANTIALIAS))
            OfficeIcon = ImageTk.PhotoImage(Image.open("assets/office.png").resize((200, 200), Image.ANTIALIAS))
            frame = customtkinter.CTkFrame(menuWindow, width=1000, height=800)
            frame.place(relx=0, rely=0)
            self.exit=ImageTk.PhotoImage(Image.open("assets/exit.png").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 20), image=EmployeeIcon, master=frame, fg_color="white",
                                    text_color="black", text="Employee", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [self.EmployeeMenu(), frame.destroy()]).place(relx=0.5, rely=0.15,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 20), image=CustomerIcon, master=frame, fg_color="white",
                                    text_color="black", text="Customer", width=80,
                                    corner_radius=50, height=70, compound="top",command=lambda: [self.CustomerMenu(), frame.destroy()]).place(relx=0.5, rely=0.4,
                                                                                       anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 20), image=OfficeIcon, master=frame, fg_color="white",
                                    text_color="black", text="Office", width=80,
                                    corner_radius=50, height=70, compound="top",command=lambda: [self.OfficeMenu(), frame.destroy()]).place(relx=0.5, rely=0.65,
                                                                                       anchor='center')

            self.back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.exit, master=self.parentWindow, fg_color="white",
                                    text_color="black", text="Exit", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=self.parentWindow.destroy).place(relx=0.9, rely=0.1, anchor='center')
            save = ImageTk.PhotoImage(Image.open("assets/save.png").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=save, master=self.parentWindow,
                                    fg_color="white",
                                    text_color="black", text="Save Data.", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: [self.saveUser() ]).place(relx=0.9, rely=0.3, anchor='center')
            menuWindow.mainloop()
        except Exception as E:
            print("Problem with type window.", E)

    def EmployeeMenu(self):
        try:
            menuWindow = self.parentWindow
            employeeWindow = UserEmployeeGUI(menuWindow, self.parentWindow, self.__userData)
            frame = customtkinter.CTkFrame(menuWindow, width=1000, height=800)
            frame.place(relx=0, rely=0)
            addIcon = ImageTk.PhotoImage(Image.open("assets/add.png").resize((200, 200), Image.ANTIALIAS))
            listIcon = ImageTk.PhotoImage(Image.open("assets/listIcon.png").resize((200, 200), Image.ANTIALIAS))
            changeIcon = ImageTk.PhotoImage(Image.open("assets/change.png").resize((200, 200), Image.ANTIALIAS))
            managerIcon = ImageTk.PhotoImage(Image.open("assets/setManager.png").resize((200, 200), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=addIcon, master=frame, fg_color="white",
                                    text_color="black", text="Add Employee.", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [employeeWindow.employeeChoiceMenu(), frame.destroy()]).place(relx=0.25, rely=0.25,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=listIcon, master=frame, fg_color="white",
                                    text_color="black", text="List Employees. ", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [employeeWindow.listEmployees(), frame.destroy()]).place(relx=0.75, rely=0.25,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=changeIcon, master=frame, fg_color="white",
                                    text_color="black", text="Change Salary.", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [employeeWindow.renderChangePage("salary"), frame.destroy()]).place(relx=0.2, rely=0.55,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=managerIcon, master=frame, fg_color="white",
                                    text_color="black", text='Set Manager.', width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [employeeWindow.setManager(), frame.destroy()]).place(relx=0.5, rely=0.55,
                                                                                                  anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=changeIcon, master=frame, fg_color="white",
                                    text_color="black", text='Change Workhours.', width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [employeeWindow.renderChangePage("working hours"),
                                                     frame.destroy()]).place(relx=0.8, rely=0.55,
                                                                             anchor='center')


            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.7, rely=0.05, anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.exit, master=frame,
                                    fg_color="white",
                                    text_color="black", text="Exit", width=80, corner_radius=50, height=30,
                                    compound="top",
                                    command=self.parentWindow.destroy).place(relx=0.9, rely=0.05, anchor='center')

            menuWindow.mainloop()
        except Exception as E:
            print(E)

    def CustomerMenu(self):
        try:
            menuWindow = self.parentWindow
            customerWindow = UserCustomerGUI(menuWindow, self.frame, self.__userData)
            accountWindow = UserAccountGUI(menuWindow, self.frame, self.__userData)
            frame = customtkinter.CTkFrame(menuWindow, width=1000, height=800)
            frame.place(relx=0, rely=0)
            addIcon = ImageTk.PhotoImage(Image.open("assets/add.png").resize((200, 200), Image.ANTIALIAS))
            listIcon = ImageTk.PhotoImage(Image.open("assets/listIcon.png").resize((200, 200), Image.ANTIALIAS))
            openIcon = ImageTk.PhotoImage(Image.open("assets/open.png").resize((200, 200), Image.ANTIALIAS))
            displayIcon = ImageTk.PhotoImage(Image.open("assets/display.webp").resize((200, 200), Image.ANTIALIAS))

            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=addIcon, master=frame, fg_color="white",
                                    text_color="black", text="Add Customer.", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [customerWindow.createCustomerComponent(), frame.destroy()]).place(relx=0.25, rely=0.3,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=listIcon, master=frame, fg_color="white",
                                    text_color="black", text="List Customers. ", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [customerWindow.ListCustomer(), frame.destroy()]).place(relx=0.75, rely=0.3,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=openIcon, master=frame, fg_color="white",
                                    text_color="black", text="Open Account.", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [accountWindow.openAccount(), frame.destroy()]).place(relx=0.25, rely=0.55,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=displayIcon, master=frame, fg_color="white",
                                    text_color="black", text='Display Accounts.', width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [accountWindow.listAccounts(), frame.destroy()]).place(relx=0.75, rely=0.55,
                                                                                                  anchor='center')


            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.7, rely=0.1, anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.exit, master=frame,
                                    fg_color="white",
                                    text_color="black", text="Exit", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=self.parentWindow.destroy).place(relx=0.9, rely=0.1, anchor='center')

            menuWindow.mainloop()
        except Exception as E:
            print(E)

    def OfficeMenu(self):
        try:
            menuWindow = self.parentWindow
            officeWindow = UserOfficeGUI(menuWindow, self.parentWindow, self.__userData)
            frame = customtkinter.CTkFrame(menuWindow, width=1000, height=800)
            frame.place(relx=0, rely=0)
            addIcon = ImageTk.PhotoImage(Image.open("assets/add.png").resize((200, 200), Image.ANTIALIAS))
            listIcon = ImageTk.PhotoImage(Image.open("assets/listIcon.png").resize((200, 200), Image.ANTIALIAS))
            expensesIcon = ImageTk.PhotoImage(Image.open("assets/expenses.png").resize((200, 200), Image.ANTIALIAS))

            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=addIcon, master=frame, fg_color="white",
                                    text_color="black", text="Add Office.", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [officeWindow.addOfficeOption(), frame.destroy()]).place(relx=0.25, rely=0.25,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=listIcon, master=frame, fg_color="white",
                                    text_color="black", text="List Offices. ", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [officeWindow.listOffices(), frame.destroy()]).place(relx=0.75, rely=0.25,
                                                                                                  anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 14), image=expensesIcon, master=frame, fg_color="white",
                                    text_color="black", text="Add Expenses.", width=80,
                                    corner_radius=50, height=70, compound="top",
                                    command=lambda: [officeWindow.addExpenseOption(), frame.destroy()]).place(relx=0.5, rely=0.55,
                                                                                                  anchor='center')

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.7, rely=0.09, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.exit, master=frame,
                                    fg_color="white",
                                    text_color="black", text="Exit", width=80, corner_radius=50, height=30,
                                    compound="top",
                                    command=self.parentWindow.destroy).place(relx=0.9, rely=0.1, anchor='center')

            menuWindow.mainloop()
        except Exception as E:
            print(E)

    def saveUser(self):
        try:
            if self.__currentUserIndex is not None:
                CustomerFile = open('userInfo.json')
                CustomerDict = json.load(CustomerFile)
                try:
                    CustomerList = [customer.toJSON() for customer in self.__userData.getCustomerList()]
                    EmployeeList = [employee.toJSON() for employee in self.__userData.getEmployeeList()]
                    ManagerList = [manager.toJSON() for manager in self.__userData.getManagerList()]
                    OfficeList = [office.toJSON() for office in self.__userData.getOfficeList()]
                except Exception as ex:
                    print(ex)
                    return
                CustomerDict['Users'][self.__currentUserIndex]['CustomerList'] = CustomerList
                CustomerDict['Users'][self.__currentUserIndex]['EmployeeList'] = EmployeeList
                CustomerDict['Users'][self.__currentUserIndex]['ManagerList'] = ManagerList
                CustomerDict['Users'][self.__currentUserIndex]['OfficeList'] = OfficeList
                with open('userInfo.json', 'w', encoding='utf-8') as f:
                    json.dump(CustomerDict, f, ensure_ascii=False, indent=4)
                print("User saved")
                saveDataPopup=ConfirmationPopUp("User data Saved.", self.parentWindow)
                saveDataPopup.createConfirmationPopUp()
        except Exception as E:
            print("Problem while saving user info." + E.__str__())

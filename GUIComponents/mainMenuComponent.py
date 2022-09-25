import json
import tkinter as tk
from Classes.dataHolderClass import dataHolder
from .EmployeeComponents import UserEmployeeGUI
from .CustomerComponents import UserCustomerGUI
from .AccountComponents import UserAccountGUI
from .OfficeComponents import UserOfficeGUI


class UserInit:
    __username: str
    __password: str
    __userWindow: tk.Tk
    __userData: dataHolder

    def __init__(self):
        self.__currentUserIndex = None

    def initUserWindow(self):
        try:
            self.__userWindow = tk.Tk()
            self.__userWindow.title("OFFICE MANAGEMENT APPLICATION")
            self.__userWindow.geometry('450x450+400+100')
            topLogo = tk.PhotoImage(file='assets/logo.png')
            self.__userWindow.iconphoto(False, topLogo)
            userNameText = tk.StringVar()
            emailText = tk.StringVar()
            tk.Label(self.__userWindow, text='UserName:').place(relx=0.5, rely=0.2, anchor='center')
            tk.Entry(self.__userWindow, textvariable=userNameText).place(relx=0.5, rely=0.25, anchor='center')
            tk.Label(self.__userWindow, text='Email:').place(relx=0.5, rely=0.3, anchor='center')
            tk.Entry(self.__userWindow, textvariable=emailText).place(relx=0.5, rely=0.35, anchor='center')
            tk.Button(self.__userWindow, text='OK',
                      command=lambda: [self.checkUser(userNameText.get(), emailText.get())],
                      fg='black',
                      bg='white').place(relx=0.5, rely=0.4,
                                        anchor='center')
            self.__userWindow.mainloop()
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
                self.__userWindow.geometry('800x800+300+000')
                self.userMainMenu()
        except Exception as E:
            print("Problem while checking user credentials.", E)

    def createUser(self):
        try:
            CustomerFile = open('userInfo.json')
            CustomerDict = json.load(CustomerFile)
            newUser = dict()
            newUser['Email'] = self.__username
            newUser['Password'] = self.__password
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

    def saveUser(self):
        try:
            if self.__currentUserIndex is not None:
                CustomerFile = open('userInfo.json')
                CustomerDict = json.load(CustomerFile)
                CustomerList = [customer.toJSON() for customer in self.__userData.getCustomerList()]
                EmployeeList = [employee.toJSON() for employee in self.__userData.getEmployeeList()]
                ManagerList = [manager.toJSON() for manager in self.__userData.getManagerList()]
                OfficeList = [office.toJSON() for office in self.__userData.getOfficeList()]
                CustomerDict['Users'][self.__currentUserIndex]['CustomerList'] = CustomerList
                CustomerDict['Users'][self.__currentUserIndex]['EmployeeList'] = EmployeeList
                CustomerDict['Users'][self.__currentUserIndex]['ManagerList'] = ManagerList
                CustomerDict['Users'][self.__currentUserIndex]['OfficeList'] = OfficeList
                with open('userInfo.json', 'w', encoding='utf-8') as f:
                    json.dump(CustomerDict, f, ensure_ascii=False, indent=4)
                print("User saved")
        except Exception as E:
            print("Problem while saving user info." + E.__str__())

    def userMainMenu(self):
        frame = tk.Frame(self.__userWindow, width=800, height=800)
        frame.place(relx=0, rely=0)
        employeeWindow = UserEmployeeGUI(self.__userWindow, frame, self.__userData)
        customerWindow = UserCustomerGUI(self.__userWindow, frame, self.__userData)
        accountWindow = UserAccountGUI(self.__userWindow, frame, self.__userData)
        officeWindow= UserOfficeGUI(self.__userWindow, frame, self.__userData)
        canvas = tk.Canvas(frame, bg='#FFFFFF', width=800, height=800, scrollregion=(0, 0, 800, 800))
        h = tk.Scrollbar(frame)
        h.pack(fill='y', side='right')
        h.config(command="canvas.yview")
        canvas.config(yscrollcommand=h.set)
        canvas.pack(side="left", expand=True, fill="both")

        tk.Button(canvas, text='Add an employee.', command=lambda: employeeWindow.employeeChoiceMenu(), fg='black',
                  bg='white').place(relx=0.2, rely=0.1,
                                    anchor='center')
        tk.Button(canvas, text='List all the employees. ',
                  command=lambda: employeeWindow.listEmployees(),
                  fg='black',
                  bg='white').place(relx=0.2, rely=0.2,
                                    anchor='center')
        tk.Button(canvas, text='Change the salary for an employee.',
                  command=lambda: employeeWindow.renderChangePage("salary"),
                  fg='black',
                  bg='white').place(relx=0.2, rely=0.3,
                                    anchor='center')
        tk.Button(canvas, text='Change the worktime of an employee.',
                  command=lambda: employeeWindow.renderChangePage("working hours"), fg='black',
                  bg='white').place(relx=0.2, rely=0.4,
                                    anchor='center')

        tk.Button(canvas, text='Set Manager for an Employee', command=lambda: employeeWindow.setManager(), fg='black',
                  bg='white').place(relx=0.2, rely=0.5,
                                    anchor='center')
        tk.Button(canvas, text='Create a customer.', command=lambda: customerWindow.createCustomerComponent(),
                  fg='black',
                  bg='white').place(relx=0.2, rely=0.6,
                                    anchor='center')
        tk.Button(canvas, text='List all the customers.',
                  command=lambda: customerWindow.ListCustomer(),
                  fg='black',
                  bg='white').place(relx=0.8, rely=0.1,
                                    anchor='center')
        tk.Button(canvas, text='Open an account for a customer.', command=lambda: accountWindow.openAccount(),
                  fg='black',
                  bg='white').place(relx=0.8, rely=0.2,
                                    anchor='center')
        tk.Button(canvas, text='Display the money in an account.', command=lambda: accountWindow.listAccounts(),
                  fg='black',
                  bg='white').place(relx=0.8, rely=0.3,
                                    anchor='center')

        tk.Button(canvas, text='Add an office.', command=lambda: officeWindow.addOfficeOption(), fg='black',
                  bg='white').place(relx=0.8, rely=0.4,
                                    anchor='center')
        tk.Button(canvas, text='List all the offices.', command=lambda: officeWindow.listOffices(), fg='black',
                  bg='white').place(relx=0.8, rely=0.5,
                                    anchor='center')
        tk.Button(canvas, text='Add expenses to a certain office.', command=lambda: officeWindow.addExpenseOption(),
                  fg='black',
                  bg='white').place(relx=0.8, rely=0.6,
                                    anchor='center')
        tk.Button(canvas, text='Save', command=lambda: self.saveUser(), fg='black',
                  bg='white').place(relx=0.7, rely=0.7,
                                    anchor='center')
        tk.Button(canvas, text='Exit', command=lambda: self.__userWindow.destroy(), fg='black',
                  bg='white').place(relx=0.5, rely=0.7,
                                    anchor='center')

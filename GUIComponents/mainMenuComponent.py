import tkinter as tk
from Classes import EmployeeSubclasses, EmployeeClass, CustomerClass, OfficeClass
from Classes.AccountClass import Account
from Services.AccountServices import displayMoney
from Services.OfficeServices import listOffices, OfficeList
from .AccountComponents import openAccount
from .EmployeeComponents import renderChangePage
from .EmployeeComponents import addEmployeeOption
from .EmployeeComponents import setManager
from Services import EmployeeServices, CustomerServices
from .CustomerComponents import *
from .OfficeComponents import addOfficeOption, addExpenseOption
from PIL import ImageTk, Image


class AddPhoto:
    _photo: ImageTk
    _rootWindow: tk.Tk

    def __init__(self, rootWindow):
        self.img = None
        self._rootWindow=rootWindow

    def showTopPhoto(self):
        dicepic = ImageTk.PhotoImage(file="C:/Users/hp/Desktop/Company/assets/logo.jpg")

        tk.Label(self._rootWindow, image=dicepic).grid(row=4, columnspan=2)



def checkUser(rootWindow: tk.Tk, username: str, email: str):
    un = username
    email = email
    rootWindow.geometry('800x800+300+000')
    mainMenuWindow(rootWindow)


def mainMenuWindow(rootWindow: tk.Tk):
    EmployeeServices.EmployeeList.append(EmployeeSubclasses.SoftwareEngineer("Vidish", 25, "11/05/2022"))
    EmployeeServices.EmployeeList.append(EmployeeClass.Manager("Sumit", 55, "22/08/2000"))
    newAccount = Account(5000, 15423, "Checking")
    CustomerServices.CustomerList.append(CustomerClass.Customer("Raja", 27, 123456, "Retail", newAccount))
    EmployeeServices.ManagerList.append(EmployeeClass.Manager("Sumit", 55, "22/08/2000"))
    OfficeList.append(OfficeClass.Office("Prestige", "Paris", True, 5000))
    frame = tk.Frame(rootWindow, width=800, height=800)
    frame.place(relx=0, rely=0)
    #dicepic = ImageTk.PhotoImage(Image.open("C:/Users/hp/Desktop/Company/assets/logo.jpg"))
    #photoFrame = tk.Label(frame, image=dicepic)
    #photoFrame.pack()
    #newPhotoInstance = AddPhoto(rootWindow)
    #newPhotoInstance.showTopPhoto()
    canvas = tk.Canvas(frame, bg='#FFFFFF', width=800, height=800, scrollregion=(0, 0, 800, 800))
    h = tk.Scrollbar(frame)
    h.pack(fill='y', side='right')
    h.config(command="canvas.yview")
    canvas.config(yscrollcommand=h.set)
    canvas.pack(side="left", expand=True, fill="both")

    tk.Button(canvas, text='Add an employee.', command=lambda: addEmployeeOption(rootWindow, frame), fg='black',
              bg='white').place(relx=0.2, rely=0.1,
                                anchor='center')
    tk.Button(canvas, text='List all the employees. ',
              command=lambda: EmployeeServices.listEmployees(rootWindow, frame),
              fg='black',
              bg='white').place(relx=0.2, rely=0.2,
                                anchor='center')
    tk.Button(canvas, text='Change the salary for an employee.',
              command=lambda: renderChangePage(rootWindow, frame, "salary"),
              fg='black',
              bg='white').place(relx=0.2, rely=0.3,
                                anchor='center')
    tk.Button(canvas, text='Change the worktime of an employee.',
              command=lambda: renderChangePage(rootWindow, frame, "working hours"), fg='black',
              bg='white').place(relx=0.2, rely=0.4,
                                anchor='center')
    tk.Button(canvas, text='Set Manager for an Employee', command=lambda: setManager(rootWindow, frame), fg='black',
              bg='white').place(relx=0.2, rely=0.5,
                                anchor='center')
    tk.Button(canvas, text='Create a customer.', command=lambda: createCustomerComponent(rootWindow, frame), fg='black',
              bg='white').place(relx=0.2, rely=0.6,
                                anchor='center')
    tk.Button(canvas, text='List all the customers.', command=lambda: CustomerServices.listCustomers(rootWindow, frame),
              fg='black',
              bg='white').place(relx=0.8, rely=0.1,
                                anchor='center')
    tk.Button(canvas, text='Open an account for a customer.', command=lambda: openAccount(rootWindow, frame),
              fg='black',
              bg='white').place(relx=0.8, rely=0.2,
                                anchor='center')
    tk.Button(canvas, text='Display the money in an account.', command=lambda: displayMoney(rootWindow, frame),
              fg='black',
              bg='white').place(relx=0.8, rely=0.3,
                                anchor='center')
    tk.Button(canvas, text='Add an office.', command=lambda: addOfficeOption(rootWindow, frame), fg='black',
              bg='white').place(relx=0.8, rely=0.4,
                                anchor='center')
    tk.Button(canvas, text='List all the offices.', command=lambda: listOffices(rootWindow, frame), fg='black',
              bg='white').place(relx=0.8, rely=0.5,
                                anchor='center')
    tk.Button(canvas, text='Add expenses to a certain office.', command=lambda: addExpenseOption(rootWindow, frame),
              fg='black',
              bg='white').place(relx=0.8, rely=0.6,
                                anchor='center')
    tk.Button(canvas, text='Exit', command=lambda: rootWindow.destroy(), fg='black',
              bg='white').place(relx=0.5, rely=0.7,
                                anchor='center')

import tkinter as tk
from tkinter import ttk

import customtkinter
from PIL import ImageTk, Image

from PopUps.ErrorPopUp import ErrorPopUp
from PopUps.ConfirmationPopUp import ConfirmationPopUp

from Services.OfficeServices import OfficeService


class UserOfficeGUI:
    _rootWindow: tk.Tk
    _parentFrame: tk.Frame
    _OfficeService: OfficeService

    def __init__(self, rootWindow, Frame, userData):
        self._rootWindow = rootWindow
        self._parentFrame = Frame
        self.confirm = ImageTk.PhotoImage(Image.open("assets/confirm.webp").resize((50, 50), Image.ANTIALIAS))
        self.back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))
        self._OfficeService = OfficeService(userData)

    def addOfficeOption(self):
        try:
            frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
            frame.grid(row=0, column=0, sticky='news')
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                   text_color="black", text="What type of office would you like to add??", width=100,
                                   corner_radius=50, height=30, compound="top").place(relx=0.5, rely=0.2,
                                                                                      anchor='center')
            international = ImageTk.PhotoImage(Image.open("assets/local.png").resize((50, 50), Image.ANTIALIAS))
            local = ImageTk.PhotoImage(Image.open("assets/international.webp").resize((50, 50), Image.ANTIALIAS))
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=international, master=frame, fg_color="white",
                                    text_color="black", text="International", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.renderMenuForOffice(frame, True)).place(
                                    relx=0.4, rely=0.3, anchor='center')
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=local, master=frame, fg_color="white",
                                    text_color="black", text="Local", width=80, corner_radius=50, height=70,
                                    compound="top",
                                    command=lambda: self.renderMenuForOffice(frame, False)).place(
                relx=0.6, rely=0.3, anchor='center')
        except Exception as E:
            print(E)

    def renderMenuForOffice(self, frame, choice):
        name = tk.StringVar()
        location = tk.StringVar()
        employeeCount = tk.IntVar()
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                               text_color="black", text="Enter the name of the office:", width=100,
                               corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.4,
                                                                                  anchor='center')
        customtkinter.CTkEntry(frame, textvariable=name, border_color="white", corner_radius=5,
                               text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                      rely=0.4,
                                                                                                      anchor='center')
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                               text_color="black", text="Enter the location of the office:", width=100,
                               corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.5,
                                                                                  anchor='center')
        customtkinter.CTkEntry(frame, textvariable=location, border_color="white", corner_radius=5,
                               text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                      rely=0.5,
                                                                                                      anchor='center')
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                               text_color="black", text="Enter the number of employees in the office:", width=100,
                               corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.65,
                                                                                  anchor='center')
        customtkinter.CTkEntry(frame, textvariable=employeeCount, border_color="white", corner_radius=5,
                               text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                      rely=0.65,
                                                                                                      anchor='center')
        officeCreationPopUp = ConfirmationPopUp()
        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.confirm, master=frame, fg_color="white",
                                text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=lambda: [officeCreationPopUp.createConfirmationPopUp("Office Created."),self._OfficeService.addOffice(name.get(), location.get(), True,
                                                                 employeeCount.get()) if choice else
                                   self._OfficeService.addOffice(name.get(), location.get(), False, employeeCount.get())
                      , frame.destroy()]).place(relx=0.2, rely=0.75, anchor='center')
        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.4, rely=0.75, anchor='center')

    def listOffices(self):
        try:
            frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
            frame.grid(row=0, column=0, sticky='news')
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
            table['columns'] = ('Name', 'Location', 'Type', "Employee Count", "Expenses", "Limit")
            table.column("#0", width=0, stretch="no")
            table.column("Name", anchor="center", width=200)
            table.column("Location", anchor="center", width=200)
            table.column("Type", anchor="center", width=200)
            table.column("Employee Count", anchor="center", width=200)
            table.column("Expenses", anchor="center", width=120)
            table.column("Limit", anchor="center", width=200)

            table.heading("#0", text="", anchor="center")
            table.heading("Name", text="Name", anchor="center")
            table.heading("Location", text="Location", anchor="center")
            table.heading("Type", text="Type", anchor="center")
            table.heading("Employee Count", text="Employee Count", anchor="center")
            table.heading("Expenses", text="Expenses", anchor="center")
            table.heading("Limit", text="Limit", anchor="center")

            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                    text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                    compound="top",
                                    command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
            userOfficeInfo = self._OfficeService.listOffices()
            for i in range(len(userOfficeInfo)):
                table.insert(parent='', index='end', iid=i, text='',
                             values=userOfficeInfo[i])
        except Exception as E:
            print(E)

    def addExpenseOption(self):
        frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
        frame.grid(row=0, column=0, sticky='news')
        newExpense = tk.IntVar(frame)
        officeName = tk.StringVar(frame)
        officeNameList=self._OfficeService.returnOfficeNames()
        officeName.set("Choose Office")
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                               text_color="black", text="Pick Office:", width=100,
                               corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.2,
                                                                                  anchor='center')

        officeMenu = customtkinter.CTkOptionMenu(frame, variable=officeName, values=officeNameList,
                                                   fg_color="white", text_color="black", button_color="white")
        officeMenu.place(relx=0.5, rely=0.2, anchor='center')
        choose = ImageTk.PhotoImage(Image.open("assets/choose.png").resize((50, 50), Image.ANTIALIAS))
        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=choose, master=frame, fg_color="white",
                                text_color="black", text="Choose", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=lambda: addExpense()).place(relx=0.7, rely=0.2, anchor='center')

        def addExpense():
            customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                   text_color="black", text="Enter Expense:", width=100,
                                   corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.4,
                                                                                      anchor='center')
            customtkinter.CTkEntry(frame, textvariable=newExpense, border_color="white", corner_radius=5,
                                   text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                          rely=0.4,
                                                                                                          anchor='center')
            expenseSetPopUp=ConfirmationPopUp()
            customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.confirm, master=frame, fg_color="white",
                                text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=lambda: [expenseSetPopUp.createConfirmationPopUp("Expense Set."),
                                    self._OfficeService.setExpense(officeName.get(), newExpense.get()), frame.destroy()]).place(relx=0.5,
                                                                                                    rely=0.6,
                                                                                                    anchor='center')

        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=frame.destroy).place(relx=0.65, rely=0.6, anchor='center')
import tkinter as tk
from tkinter import ttk

import customtkinter
from PIL import Image, ImageTk

from PopUps.ErrorPopUp import ErrorPopUp
from PopUps.ConfirmationPopUp import ConfirmationPopUp
from Services.AccountServices import AccountService


class UserAccountGUI:
    frame: tk.Tk
    choice: tk.IntVar
    _rootWindow: tk.Tk
    _AccountService: AccountService

    def __init__(self, rootWindow, frame, userData):
        self.frame = frame
        self._rootWindow = rootWindow
        self._AccountService = AccountService(userData)
        self.back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))
        self.confirm = ImageTk.PhotoImage(Image.open("assets/confirm.webp").resize((50, 50), Image.ANTIALIAS))

    def openAccount(self):
        frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
        frame.grid(row=0, column=0, sticky='news')
        frame.tkraise(self.frame)
        customerName = tk.StringVar(frame, value="Pick Customer")
        nonAccountHolderList = self._AccountService.returnNonAccountNameList()
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                    text_color="black", text="Please Customer", width=100,
                    corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.2,
                                                                                  anchor='center')
        customerMenu = customtkinter.CTkOptionMenu(frame, variable=customerName, values=nonAccountHolderList,
                                                   fg_color="white", text_color="black", button_color="white")
        customerMenu.place(relx=0.5, rely=0.2, anchor='center')
        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=frame.destroy).place(relx=0.3, rely=0.65, anchor='center')
        choose = ImageTk.PhotoImage(Image.open("assets/choose.png").resize((50, 50), Image.ANTIALIAS))
        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=choose, master=frame, fg_color="white",
                                text_color="black", text="Choose", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=lambda: self.makeAccount(frame, customerName.get())).place(
            relx=0.7, rely=0.2, anchor='center')


    def makeAccount(self, frame, selectedCustomerName):
        selectedCustomer=self._AccountService.returnCustomerFromName(selectedCustomerName)
        if selectedCustomer.getAccount() is None:
            if selectedCustomer.getType() == "Retail":
                customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                       text_color="black", text="Type of Account:", width=100,
                                       corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.4,
                                                                                          anchor='center')
                self.choice = tk.IntVar()
                var = tk.StringVar()
                var.set("Choice")
                amount = tk.IntVar()
                R1 = customtkinter.CTkRadioButton(frame, text="Checking account", variable=self.choice, value=1,
                                    corner_radius=50,fg_color="white",
                                       text_color="white",
                                                  border_color="black",
                                    command=lambda: var.set("Checking"))
                R1.place(relx=0.45, rely=0.4, anchor='center')

                R2 = customtkinter.CTkRadioButton(frame, text="Savings Account", variable=self.choice, value=2,
                                                  corner_radius=50, fg_color="white",
                                                  text_color="white",
                                                  border_color="black",
                                    command=lambda: var.set("Savings"))
                R2.place(relx=0.7, rely=0.4, anchor='center')
                customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                       text_color="black", text="Enter Amount:", width=100,
                                       corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.5,
                                                                                          anchor='center')

                customtkinter.CTkEntry(frame, textvariable=amount, border_color="white", corner_radius=5,
                                       text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                              rely=0.5,
                                                                                                              anchor='center')
                AccountOpened = ConfirmationPopUp()
                customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.confirm, master=frame,
                                        fg_color="white",
                                        text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                        compound="top",
                                        command=lambda: [self._AccountService.addAccount(selectedCustomerName, amount.get(),var.get()),
                                           frame.destroy(), AccountOpened.createConfirmationPopUp("Account Opened.")]).place(relx=0.2,rely=0.65,anchor='center')
            elif selectedCustomer.getType() == "Non-Retail":
                amount = tk.StringVar()
                customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                                       text_color="black", text="Enter Loan Amount:", width=100,
                                       corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.5,
                                                                                          anchor='center')

                customtkinter.CTkEntry(frame, textvariable=amount, border_color="white", corner_radius=5,
                                       text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                              rely=0.5,
                                                                                                              anchor='center')
                customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.confirm, master=frame,
                                        fg_color="white",
                                        text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                        compound="top",
                                        command=lambda: [self._AccountService.addAccount(selectedCustomer, amount, "Loan"),
                                           frame.destroy()]).place(relx=0.2,rely=0.65, anchor='center')

        else:
            print("This customer already has an account.")

    def listAccounts(self):
        try:
            frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
            frame.grid(row=0, column=0, sticky='news')
            if len(self._AccountService.returnAccountHolderList()) > 0:
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
                table['columns'] = ('Name', 'Customer Type', 'Account Type', "Account Number", "Amount", "Interest")
                table.column("#0", width=0, stretch="no")
                table.column("Name", anchor="center", width=200)
                table.column("Customer Type", anchor="center", width=200)
                table.column("Account Type", anchor="center", width=200)
                table.column("Account Number", anchor="center", width=200)
                table.column("Amount", anchor="center", width=200)
                table.column("Interest", anchor="center", width=200)

                table.heading("#0", text="", anchor="center")
                table.heading("Name", text="Name", anchor="center")
                table.heading("Customer Type", text="Customer Type", anchor="center")
                table.heading("Account Type", text="Account Type", anchor="center")
                table.heading("Account Number", text="Account Number", anchor="center")
                table.heading("Amount", text="Amount", anchor="center")
                table.heading("Interest", text="Interest", anchor="center")
                lst = []
                customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame,
                                        fg_color="white",
                                        text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                        compound="top",
                                        command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
                accountDetailsList = self._AccountService.displayMoney()
                total_rows = len(accountDetailsList)
                for i in range(total_rows):
                    table.insert(parent='', index='end', iid=i, text='',
                                 values=accountDetailsList[i])
            else:
                tk.Label(frame, text='There are no customers').place(relx=0.2, rely=0.4, anchor='center')
        except Exception as e:
            print(e)

import tkinter as tk
from tkinter import ttk

import customtkinter
from PIL import ImageTk, Image

from PopUps.ErrorPopUp import ErrorPopUp
from PopUps.ConfirmationPopUp import ConfirmationPopUp

from Services.CustomerServices import CustomerService


class UserCustomerGUI:
    _rootWindow: tk.Tk
    _parentFrame: tk.Frame
    _CustomerService: CustomerService

    def __init__(self, rootWindow, Frame, userData):
        self._rootWindow = rootWindow
        self._parentFrame = Frame
        self._CustomerService = CustomerService(userData)
        self.back = None

    def createCustomerComponent(self):
        frame = customtkinter.CTkFrame(self._rootWindow, width=1000, height=800)
        frame.grid(row=0, column=0, sticky='news')
        name = tk.StringVar()
        age = tk.IntVar()
        aadhar = tk.IntVar()
        customerType = tk.StringVar()
        customerType.set("Pick the type of Customer")
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                               text_color="black", text="Please enter the name of the customer:", width=100,
                               corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.2,
                                                                                  anchor='center')
        customtkinter.CTkEntry(frame, textvariable=name, border_color="white", corner_radius=5,
                               text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                      rely=0.2,
                                                                                                      anchor='center')
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                               text_color="black", text="Please enter the age of the customer:", width=100,
                               corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.3,
                                                                                  anchor='center')
        customtkinter.CTkEntry(frame, textvariable=age, border_color="white", corner_radius=5,
                               text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                      rely=0.3,
                                                                                                      anchor='center')
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                               text_color="black", text="Please enter the aadhar of the customer:", width=100,
                               corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.4,
                                                                                  anchor='center')
        customtkinter.CTkEntry(frame, textvariable=aadhar, border_color="white", corner_radius=5,
                               text_color="white", width=100, height=2, text_font=("B old", 8)).place(relx=0.5,
                                                                                                      rely=0.4,
                                                                                                      anchor='center')
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 10), master=frame, fg_color="white",
                               text_color="black", text="Please choose the type of customer:", width=100,
                               corner_radius=50, height=30, compound="top").place(relx=0.2, rely=0.5,
                                                                                  anchor='center')
        customerTypeList = ('Retail', 'Non-Retail')
        customerMenu = customtkinter.CTkOptionMenu(frame,variable=customerType, values=customerTypeList, fg_color="white", text_color="black",button_color="white")
        customerMenu.place(relx=0.5, rely=0.5, anchor='center')

        back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))

        confirm = ImageTk.PhotoImage(Image.open("assets/confirm.webp").resize((50, 50), Image.ANTIALIAS))
        customerCreated = ConfirmationPopUp()
        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=back, master=frame, fg_color="white",
                                text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=frame.destroy).place(relx=0.65, rely=0.6, anchor='center')

        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=confirm, master=frame, fg_color="white",
                                text_color="black", text="Confirm", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=lambda: [
                                    self._CustomerService.createCustomer(name.get(), age.get(), aadhar.get(),
                                                                         customerType.get()),
                                    frame.destroy(), customerCreated.createConfirmationPopUp("Employee created.")]).place(relx=0.5,
                                                            rely=0.6,
                                                            anchor='center')

    def ListCustomer(self):
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
        table['columns'] = ('Name', 'Age', 'Aadhar', "Type", "Account Number")
        table.column("#0", width=0, stretch="no")
        table.column("Name", anchor="center", width=200)
        table.column("Age", anchor="center", width=120)
        table.column("Aadhar", anchor="center", width=200)
        table.column("Type", anchor="center", width=130)
        table.column("Account Number", anchor="center", width=200)

        table.heading("#0", text="", anchor="center")
        table.heading("Name", text="Name", anchor="center")
        table.heading("Age", text="Age", anchor="center")
        table.heading("Aadhar", text="Aadhar ", anchor="center")
        table.heading("Type", text="Type", anchor="center")
        table.heading("Account Number", text="Account Number", anchor="center")
        self.back = ImageTk.PhotoImage(Image.open("assets/back.png").resize((50, 50), Image.ANTIALIAS))
        customtkinter.CTkButton(text_font=("Malgun Gothic", 10), image=self.back, master=frame, fg_color="white",
                                text_color="black", text="Back", width=30, corner_radius=50, height=30,
                                compound="top",
                                command=frame.destroy).place(relx=0.5, rely=0.5, anchor='center')
        customerList = self._CustomerService.returnCustomerList()

        total_rows = len(customerList)
        for i in range(total_rows):
            table.insert(parent='', index='end', iid=i, text='',
                         values=customerList[i])

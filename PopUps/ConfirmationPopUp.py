import customtkinter


class ConfirmationPopUp:

    def createConfirmationPopUp(self, message):
        errorPopUp = customtkinter.CTkToplevel()
        errorPopUp.title("Confirm")
        errorPopUp.geometry('400x100+750+500')
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 9), master=errorPopUp, fg_color="white",
                               text_color="black", text=message, width=20,
                               corner_radius=50, height=20, compound="top").place(relx=0.5, rely=0.3,
                                                                                  anchor='center')
        customtkinter.CTkButton(errorPopUp, text='OK', fg_color="white", text_color="black",
                                command=lambda: [errorPopUp.destroy()],
                                width=10, height=10, compound="top").place(relx=0.5, rely=0.65,
                                                                           anchor='center')

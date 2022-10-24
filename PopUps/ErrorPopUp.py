import customtkinter


class ErrorPopUp:

    __errorMessage: str
    __parentWindow: customtkinter.CTk

    def __init__(self, message, parentWindow):
        self.__errorMessage = message
        self.__parentWindow = parentWindow


    def createErrorPopUp(self):
        errorPopUp = customtkinter.CTkToplevel()
        errorPopUp.title("Error")
        errorPopUp.geometry('400x100+430+350')
        customtkinter.CTkLabel(text_font=("Malgun Gothic", 9), master=errorPopUp, fg_color="white",
                               text_color="black", text=self.__errorMessage, width=20,
                               corner_radius=50, height=20, compound="top").place(relx=0.5, rely=0.3,
                                                                                  anchor='center')
        customtkinter.CTkButton(errorPopUp, text='OK', fg_color="white", text_color="black",
                                command=lambda: [errorPopUp.destroy()],
                                width=10, height=10, compound="top").place(relx=0.5, rely=0.65,
                                                                            anchor='center')


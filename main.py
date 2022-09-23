import tkinter as tk
from GUIComponents.mainMenuComponent import checkUser, AddPhoto

if __name__ == "__main__":
    try:
        window = tk.Tk()
        window.title("OFFICE MANAGEMENT APPLICATION")
        window.geometry('450x450+400+100')
        #topIcon = tk.PhotoImage(file="Any image file")
        topLogo = tk.PhotoImage(file='assets/logo.png')
        window.iconphoto(False, topLogo)
        userNameText = tk.StringVar()
        emailText = tk.StringVar()
        tk.Label(window, text='UserName:').place(relx=0.5, rely=0.2, anchor='center')
        tk.Entry(window, textvariable=userNameText).place(relx=0.5, rely=0.25, anchor='center')
        tk.Label(window, text='Email:').place(relx=0.5, rely=0.3, anchor='center')
        tk.Entry(window, textvariable=emailText).place(relx=0.5, rely=0.35, anchor='center')
        tk.Button(window, text='OK', command=lambda: checkUser(window, userNameText, emailText ), fg='black',
                  bg='white').place(relx=0.5, rely=0.4,
                                    anchor='center')
        window.mainloop()
    except Exception as error:
        print(error)

from GUIComponents.mainMenuComponent import UserInit

if __name__ == "__main__":
    try:
        newUser = UserInit()
        newUser.initUserWindow()
    except Exception as error:
        print(error)

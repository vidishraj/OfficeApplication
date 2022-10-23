from Classes.OfficeClass import Office
import tkinter as tk

from Classes.dataHolderClass import dataHolder


class OfficeService:
    _userServiceInstance: dataHolder

    def __init__(self, userInstance):
        self._userServiceInstance = userInstance

    def returnOfficeNames(self):
        return [office.getName() for office in self._userServiceInstance.getOfficeList()]

    def returnOfficeFromName(self, name):
        for office in self._userServiceInstance.getOfficeList():
            if office.getName() == name:
                return office

    def setExpense(self, Name, Expense):
        print(Name, Expense)
        office: Office =self.returnOfficeFromName(Name)
        office.addExpense(Expense)

    def addOffice(self, name, location, officeType, employeeCount):
        try:
            newOffice = Office(name, location, officeType, employeeCount)
            self._userServiceInstance.getOfficeList().append(newOffice)
        except Exception as e:
            print(e)

    def listOffices(self):
        lst = []
        for office in self._userServiceInstance.getOfficeList():
            temp = [office.getName(), office.getLocation(), office.getTypeString(), office.getEmployeeCount(),
                    office.getExpense(), 2000000]
            lst.append(temp)
        return lst

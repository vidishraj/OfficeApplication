from Classes.AccountClass import Account
from Classes.CustomerClass import Customer
from Classes.EmployeeSubclasses import SoftwareEngineer, ITstaff, Maid, Architect
from Classes.EmployeeClass import Manager
from Classes.OfficeClass import Office
from datetime import datetime
from logger import logging

logger = logging.getLogger('Office Application')


class dataHolder:
    __EmployeeList: list = []
    __CustomerList: list = []
    __OfficeList: list = []
    __ManagerList: list = []

    def getEmployeeList(self):
        return self.__EmployeeList

    def getCustomerList(self):
        return self.__CustomerList

    def getManagerList(self):
        return self.__ManagerList

    def getOfficeList(self):
        return self.__OfficeList

    def setEmployeeList(self, EmployeeList):
        try:
            for employee in EmployeeList:
                newEmp = None
                employeeJoining = datetime.strptime(employee['joiningDate'], '%d/%m/%Y')
                if employee['type'] == "createSoftwareEngineer":
                    newEmp = SoftwareEngineer(employee['name'], employee['age'], employeeJoining,
                                              employee['type'])
                if employee['type'] == "createManager":
                    newEmp = SoftwareEngineer(employee['name'], employee['age'], employeeJoining,
                                              employee['type'])
                    self.__ManagerList.append(newEmp)
                elif employee['type'] == "createITStaff":
                    newEmp = ITstaff(employee['name'], employee['age'], employeeJoining, employee['type'])
                elif employee['type'] == "createMaid":
                    newEmp = Maid(employee['name'], employee['age'], employeeJoining, employee['type'])
                elif employee['type'] == "createArchitect":
                    newEmp = Architect(employee['name'], employee['age'], employeeJoining, employee['type'])
                if employee['manager'] is not None:
                    newEmp = Manager(employee['name'], employee['age'], employeeJoining, employee['type'])
                    newEmp.addManager(newEmp)
                self.__EmployeeList.append(newEmp)
        except Exception as E:
            logger.error(f"Error while setting employee list. {E}")

    def setCustomerList(self, CustomerList):
        try:
            for customer in CustomerList:
                if customer["accountDetails"] is not None:
                    accountOpeningTime = datetime.strptime(customer["accountDetails"]["timeOfAccountOpening"],
                                                           "%d/%m/%y %H:%M:%S")
                    newAccount = Account(customer["accountDetails"]["initDeposit"],
                                         customer["accountDetails"]["accountNumber"],
                                         customer["accountDetails"]["accountType"])
                    newAccount.setAccountOpeningTime(accountOpeningTime)
                    newCustomer = Customer(customer["name"], customer["age"], customer["aadhar"],
                                           customer["typeOfAccount"], newAccount)
                    self.__CustomerList.append(newCustomer)
                else:
                    newCustomer = Customer(customer["name"], customer["age"], customer["aadhar"],
                                           customer["typeOfAccount"], None)
                    self.__CustomerList.append(newCustomer)
        except Exception as E:
            logger.error(E)

    def setOfficeList(self, OfficeList):
        try:
            for office in OfficeList:
                newOffice = Office(office["name"], office["location"], office["officeType"], office["employeeCount"])
                self.__OfficeList.append(newOffice)
        except Exception as E:
            logger.error("Error setting office list in data holder.")

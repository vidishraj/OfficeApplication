from Classes import EmployeeSubclasses, EmployeeClass
from Classes.dataHolderClass import dataHolder


class EmployeeService:
    _userServiceInstance: dataHolder

    def __init__(self, userInstance):
        self._userServiceInstance = userInstance

    def insertEmployee(self, name, age, dateOfJoining, choice):
        newEmp = None
        if choice == "createMaid":
            newEmp = EmployeeSubclasses.Maid(name, age, dateOfJoining, choice)
        elif choice == "createSoftwareEngineer":
            newEmp = EmployeeSubclasses.SoftwareEngineer(name, age, dateOfJoining, choice)
        elif choice == "createArchitect":
            newEmp = EmployeeSubclasses.Architect(name, age, dateOfJoining, choice)
        elif choice == "createManager":
            newEmp = EmployeeClass.Manager(name, age, dateOfJoining, choice)
            self._userServiceInstance.getManagerList().append(newEmp)
        elif choice == "createITStaff":
            newEmp = EmployeeSubclasses.ITstaff(name, age, dateOfJoining, choice)
        if newEmp is not None:
            self._userServiceInstance.getEmployeeList().append(newEmp)
        return newEmp

    def returnEmployeeList(self, ):
        employeeList = []
        for Employee in self._userServiceInstance.getEmployeeList():
            managerName = ""
            if Employee.getManager() is not None:
                managerName = Employee.getManager().getName()

            temp = [Employee.getName(), Employee.getSalary(), Employee.getWorkingHours(), managerName,
                    Employee.getAge(),
                    Employee.getDOJ()]
            employeeList.append(temp)
        return employeeList

    def returnEmployeeNameList(self, ):
        return [Employee.getName() for Employee in self._userServiceInstance.getEmployeeList()]

    def returnEmployeeFromName(self, name):
        for Employee in self._userServiceInstance.getEmployeeList():
            if Employee.getName() == name:
                return Employee
        return None

    def returnManagerNameList(self, ):
        return [Manager.getName() for Manager in self._userServiceInstance.getManagerList()]

    def returnManagerFromName(self, name):
        for Manager in self._userServiceInstance.getManagerList():
            if Manager.getName() == name:
                return Manager
        return None

    def changeSalary(self, employeeName, salary):
        employee = self.returnEmployeeFromName(employeeName)
        employee.setSalary(salary)

    def changeWorktime(self, employeeName, workHours):
        manager: EmployeeClass.Employee = self.returnEmployeeFromName(employeeName)
        manager.setWorkingHours(workHours)

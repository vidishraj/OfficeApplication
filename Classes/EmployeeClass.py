from datetime import date
from multiprocessing import managers
#from EmployeeCollector import EmployeeSubclasses
class Employee:

    _name:str
    _age:int
    _salary:int
    _workinghours:int
    _dateOfJoining:date
    _Manager=None
    _isAdmin:bool=False
    
    def __init__(self, name , age, joiningDate) -> None:
        self._name=name
        self._age=age
        self._dateOfJoining=joiningDate

    
    def setSalary(self,newSalary:int):
        self._salary=newSalary
        print(f"Salary has been set for the employee {self._name}\n")
        return
    
    def setWorkingHours(self, newHours:int):
        self._workinghours=newHours
        print(f"New working hours have been set for the employee {self._name}\n")
        return
    
    def getName(self):
        return self._name

    def getDOJ(self):
        return self._dateOfJoining

    def getAge(self):
        return self._age
    
    def getSalary(self):
        return self._salary
    
    def getWorkingHours(self):
        return self._workinghours

    def addManager(self, Manager):
        self._Manager=Manager

    def getManager(self):
        return self._Manager

class Manager(Employee):

    _EmployeesUnder:list=[]

    def __init__(self, name, age, joiningDate) -> None:
        super().__init__(name, age, joiningDate)
        self._salary=200000
        self._workinghours=9

    def addEmployee(self,Employee):
        self._EmployeesUnder.append(Employee)
    
    def getEmployeeUnder(self):
        return self._EmployeesUnder


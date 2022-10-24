from datetime import date


class Employee:
    _name: str
    _age: int
    _salary: int
    _workinghours: int
    _dateOfJoining: date
    _Manager = None
    _isAdmin: bool = False
    _type: str

    def __init__(self, name, age, joiningDate, EmployeeType) -> None:
        self._type = EmployeeType
        self._name = name
        self._age = age
        self._dateOfJoining = joiningDate

    def toJSON(self):
        try:
            selfJSon = dict()
            selfJSon['name'] = self._name
            selfJSon['age'] = self._age
            selfJSon['joiningDate'] = self._dateOfJoining.strftime("%d/%m/%Y")
            selfJSon['salary'] = self._salary
            selfJSon['workinghours'] = self._workinghours
            selfJSon['type'] = self._type
            selfJSon['manager'] = self._Manager.toJSON() if self._Manager is not None else None
            return selfJSon
        except Exception as ex:
            print("hello")

    def setSalary(self, newSalary: int):
        self._salary = newSalary
        print(f"Salary has been set for the employee {self._name}\n")
        return

    def setWorkingHours(self, newHours: int):
        self._workinghours = newHours
        print(f"New working hours have been set for the employee {self._name}\n")
        return

    def getName(self):
        return self._name

    def getDOJ(self):
        return self._dateOfJoining.strftime("%d/%m/%Y")


    def getAge(self):
        return self._age

    def getSalary(self):
        return self._salary

    def getWorkingHours(self):
        return self._workinghours

    def addManager(self, manager):
        self._Manager = manager

    def getManager(self):
        return self._Manager


class Manager(Employee):
    _EmployeesUnder: list = []

    def __init__(self, name, age, joiningDate, EmployeeType) -> None:
        super().__init__(name, age, joiningDate, EmployeeType)
        self._salary = 200000
        self._workinghours = 9

    def addEmployee(self, employee):
        self._EmployeesUnder.append(employee)

    def getEmployeeUnder(self):
        return self._EmployeesUnder

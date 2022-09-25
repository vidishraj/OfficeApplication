from .EmployeeClass import Employee


class SoftwareEngineer(Employee):

    def __init__(self, name, age, joiningDate, EmployeeType) -> None:
        super().__init__(name, age, joiningDate, EmployeeType)
        self._salary = 100000
        self._workinghours = 7


class Maid(Employee):

    def __init__(self, name, age, joiningDate, EmployeeType) -> None:
        super().__init__(name, age, joiningDate, EmployeeType)
        self._salary = 20000
        self._workinghours = 5


class Architect(Employee):

    def __init__(self, name, age, joiningDate, EmployeeType) -> None:
        super().__init__(name, age, joiningDate, EmployeeType)
        self._salary = 80000
        self._workinghours = 8


class ITstaff(Employee):

    def __init__(self, name, age, joiningDate, EmployeeType) -> None:
        super().__init__(name, age, joiningDate, EmployeeType)
        self._salary = 50000
        self._workinghours = 6
        self._isAdmin = True

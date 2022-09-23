class Office:
    _Name: str
    _Location: str
    _type: bool
    _EmployeeCount: int
    _limitReached: bool = False
    _expense: int = 0

    def __init__(self, name, location, type, count) -> None:
        self._Name = name
        self._Location = location
        self._type = type
        self._EmployeeCount = count

    def checkLimit(self):
        if self._type and self._expense >= 100000:
            self._limitReached = True
        elif not self._type and self._expense >= 200000:
            self._limitReached = True

    def getName(self):
        return self._Name

    def getLocation(self):
        return self._Location

    def getExpense(self):
        return self._expense

    def getType(self):
        return self._type

    def getEmployeeCount(self):
        return self._EmployeeCount

    def getTypeString(self):
        if self._type:
            return "International"
        return "Local"

    def addExpense(self, expense):
        self.checkLimit()
        if self._limitReached:
            print("Limit has been reached. Expenses not allowed.")
        self._expense += expense

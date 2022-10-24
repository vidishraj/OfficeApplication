from PopUps.ErrorPopUp import ErrorPopUp
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

    def toJSON(self):
        selfJSon = dict()
        selfJSon['name'] = self._Name
        selfJSon['location'] = self._Location
        selfJSon['officeType'] = self._type
        selfJSon['employeeCount'] = self._EmployeeCount
        selfJSon['expense'] = self._expense
        return selfJSon
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
            limitError = ErrorPopUp("Limit has been reached. Additional Expenses not allowed.", None)
            limitError.createErrorPopUp()
        self._expense += expense

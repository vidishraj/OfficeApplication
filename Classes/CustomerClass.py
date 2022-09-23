from datetime import datetime
from .AccountClass import Account
from Exceptions.WrongInputException import WrongInputException

class Customer:

    _name:str
    _age:int
    _aadharNumber:int
    _account:Account=None
    typeOfAccount:str=None

    def __init__(self, name , age, aadhar, type, accountdeets) -> None:
        self._name=name
        self._age=age
        self._aadharNumber=aadhar
        self.typeOfAccount=type
        if accountdeets==None:
            self._account=None
        else:
            self._account=accountdeets

    def getAge(self):
        return self._age

    def getName(self):
        return self._name

    def getType(self):
        return self.typeOfAccount
    
    def getAadhar(self):
        return self._aadharNumber

    def setAccount(self, accountDeets):
        if(self._account==None):
            self._account=accountDeets
        else:
            print("The customer already has an account.")

    def getAccount(self):
        return self._account
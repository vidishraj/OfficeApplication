from datetime import date, datetime
from logger import logging

logger = logging.getLogger('Office Application')


class Account:
    _accountNumber: int
    _Deposit: int = 0
    _initDeposit: int = 0
    _type: str
    _timeOfAccountOpening: date

    def __init__(self, initDeposit, accountNumber, accountType):
        self._accountNumber = accountNumber
        self._Deposit = initDeposit
        self._initDeposit = initDeposit
        self._type = accountType
        self._timeOfAccountOpening = datetime.now()

    def toJSON(self):
        try:
            selfJSon = dict()
            selfJSon['accountNumber'] = self._accountNumber
            selfJSon['Deposit'] = self._Deposit
            selfJSon['initDeposit'] = self._initDeposit
            selfJSon['accountType'] = self._type
            selfJSon['timeOfAccountOpening'] = self._timeOfAccountOpening.strftime("%d/%m/%y %H:%M:%S")
            return selfJSon
        except Exception as ex:
            logger.error("Problem while serialising customer data.")

    def setAccountOpeningTime(self, time):
        self._timeOfAccountOpening = time

    def latestBalance(self):
        minutes_diff = int((datetime.now() - self._timeOfAccountOpening).total_seconds() / 60.0)
        if self._type == "Checking":
            self._Deposit += int((0.05 * self._Deposit) * minutes_diff)
        elif self._type == "Savings":
            self._Deposit += int((0.08 * self._Deposit) * minutes_diff)
        elif self._type == "Loan":
            self._Deposit -= int((0.09 * self._Deposit) * minutes_diff)
            if self._Deposit <= 0:
                self._Deposit = 0
                logger.info(f"The Loan account with the account number {self._accountNumber} has been payed.")
        return self._Deposit

    def getDeposit(self):
        return self._initDeposit

    def getType(self):
        return self._type

    def getAccountNumber(self):
        return self._accountNumber

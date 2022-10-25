from random import randint
from Classes.AccountClass import Account
from Classes.dataHolderClass import dataHolder
from logger import logging

logger = logging.getLogger('Office Application')


class AccountService:
    _userServiceInstance: dataHolder

    def __init__(self, userInstance):
        self._userServiceInstance = userInstance

    def addAccount(self, CustomerName, initDeposit, typeOfAccount):
        try:
            Customer = self.returnCustomerFromName(CustomerName)
            accountNumber: int = randint(10000, 99999)
            newAccount: Account = Account(initDeposit, accountNumber, typeOfAccount)
            Customer.setAccount(newAccount)
            logger.info("Account set.")
        except Exception as e:
            logger.error(f"Error in services for adding account {e}")

    def returnAccountHolderList(self):
        AccountList = []
        for customer in self._userServiceInstance.getCustomerList():
            if customer.getAccount() is not None:
                AccountList.append(customer.getName())
            return AccountList

    def returnNonAccountNameList(self, ):
        nonAccountList = []
        for customer in self._userServiceInstance.getCustomerList():
            if customer.getAccount() is None:
                nonAccountList.append(customer.getName())
                return nonAccountList

    def returnCustomerFromName(self, name):
        for customer in self._userServiceInstance.getCustomerList():
            if customer.getName() == name:
                return customer
        return None

    def returnManagerNameList(self, ):
        return [Manager.getName() for Manager in self._userServiceInstance.getManagerList()]

    def displayMoney(self):
        try:
            accountList = []
            resultList = []
            for customer in self._userServiceInstance.getCustomerList():
                if customer.getAccount() is not None:
                    cust = {'name': customer.getName(), 'customerType': customer.getType(),
                            'account': customer.getAccount()}
                    accountList.append(cust.copy())
            for account in accountList:
                temp = [account['name'], account['customerType'], account['account'].getType(),
                        account['account'].getAccountNumber(), account['account'].latestBalance(),
                        account['account'].latestBalance() - account['account'].getDeposit()]
                resultList.append(temp)
            return resultList
        except Exception as e:
            logger.error(f"Problem in services for displaying money. {e}")

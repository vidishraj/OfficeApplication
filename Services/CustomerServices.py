from Classes.CustomerClass import Customer
from Classes.dataHolderClass import dataHolder
from logger import logging

logger = logging.getLogger('Office Application')


class CustomerService:
    _userServiceInstance: dataHolder

    def __init__(self, userInstance):
        self._userServiceInstance = userInstance

    def createCustomer(self, name, age, aadhar, typeOfAccount):
        try:
            newCustomer = Customer(name, age, aadhar, typeOfAccount, None)
            self._userServiceInstance.getCustomerList().append(newCustomer)
        except Exception as e:
            logger.error(f"Problem in services for creating customer. {e}")

    def returnCustomerList(self):
        CustomerNameList = []
        for customer in self._userServiceInstance.getCustomerList():
            accountNumber = 0
            if customer.getAccount() is not None:
                accountNumber = customer.getAccount().getAccountNumber()

            temp = [customer.getName(), customer.getAge(), customer.getAadhar(), customer.getType(), accountNumber]
            CustomerNameList.append(temp)
        return CustomerNameList

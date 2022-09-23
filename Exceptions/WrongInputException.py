

class WrongInputException(Exception):


    def _init__(self):
        self.__str__=("You have entered a value that does not match the required value. Please enter again.")
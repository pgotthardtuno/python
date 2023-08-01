class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if float(amount) <= 0:
            return False
        else:
            self.__account_balance += float(amount)
            return True

    def withdraw(self, amount):
        if float(amount) <= 0:
            return False
        elif float(amount) > self.__account_balance:
            return False
        else:
            self.__account_balance -= float(amount)
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

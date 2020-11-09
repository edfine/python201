class BankAccount():
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("can't deposit nonpositive amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("can't withdraw", amount, "or you would be overdrawn!")
        else:
            print("can't withdraw nonpositive amount!")


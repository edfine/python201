class BankAccount():
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    'representation of the object "feedable" to Python interpreter'
    def __repr__(self):
        return self.__class__.__name__ + '(' + repr(self.name) \
               + ', ' + repr(self.balance) + ')'

    ''''string representation of object, for humans
    __repr__ is used if __str__ does not exist'''
    def __str__(self):
        print('in the __str__() function')
        return self.name + ' ' + str(self.balance)

    def __add__(self, other):
        return BankAccount(self.name + ' ' + other.name, \
				self.balance + other.balance)
    def __len__(self):
        return self.balance
    
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


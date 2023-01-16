class BankAccount():
    def __init__(self, owner, balance: float):
        self.w_amount = None
        self.owner = owner
        self.balance = balance
        '''This is the constructor for the class. It should initialize the owner and balance instance variables.'''

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        return self.balance

    def withdraw(self, w_amount):
        self.w_amount = w_amount
        if self.w_amount > self.balance:
            print (f"you don't have enough balance to withdraw {self.w_amount}")
        elif self.w_amount <= self.balance:
            self.balance -= self.w_amount



    def check_balance(self):
        return self.balance

acct = BankAccount("Jane Smith", 1000)
print(acct.check_balance())  # 1000
acct.deposit(500)
print(acct.check_balance())  # 1500
acct.withdraw(200)
print(acct.check_balance())  # 1300
acct.withdraw(2000) # It should print an error message.

'''In this example you created the BankAccount class with three methods: __init__, deposit, withdraw and check_balance. 
The __init__ method is the constructor, which initializes the owner and balance instance variables. The deposit 
method increases the balance by the given amount. The withdraw method decreases the balance by the given amount, 
but only if the withdrawn amount is less than or equal to the current balance, if not return a message that says that. 
The check_balance method returns the current balance.'''

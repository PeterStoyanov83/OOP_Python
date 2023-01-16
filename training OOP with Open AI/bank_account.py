class BankAccount:
    def __init__(self, acc_number: str, balance: float, acc_holder: str):
        self.acc_number = acc_number
        self.balance = balance
        self.acc_holder = acc_holder

    def deposit(self, amount: float):
        self.balance += amount
        return self.balance

    def withraw(self, amount: float):
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

    def __repr__(self):
        return f"Account number: {self.acc_number}, Balance: {self.balance}, Account holder: {self.acc_holder}"

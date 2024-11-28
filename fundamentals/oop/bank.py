class BankAccount:

    bank_name = "First National Dojo"

    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance


    def withdraw(self,amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

    def deposit(self,amount):
        self.balance += amount
        return self

    def display_account_info(self):
        print(f"your balance is {self.balance} with interest rate {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        else:
            self.balance=self.balance
        return self

    
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line


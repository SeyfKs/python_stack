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


account1 = BankAccount(0.1, 1000 )
account2 = BankAccount(0.13, 4000 )

account1.deposit(1000).deposit(300).deposit(1600).withdraw(1550).yield_interest().display_account_info()
account2.deposit(2000).deposit(300).withdraw(1350).withdraw(50).withdraw(2050).withdraw(150).yield_interest().display_account_info()
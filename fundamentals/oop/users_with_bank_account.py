class BankAccount:

    bank_name = "First National Dojo"

    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance

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
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self,amount):
        self.account.balance += amount
        return self
    
    def make_withdrawl(self,amount):
        if BankAccount.can_withdraw(self.account.balance,amount):
            self.account.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account.balance}")
        return self



user1 = User("Sabrina","sab.harvey@gmail.com")
user2= User("Mark","mrk.lw@gmail.com")
user1.make_deposit(1000).make_withdrawl(300).display_user_balance()
user2.make_deposit(4500).make_withdrawl(3000).display_user_balance()
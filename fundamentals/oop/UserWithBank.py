class BankAccount:
    bank_name = "First National Dojo"
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        return True


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}  # Dictionary to hold multiple accounts

    def add_account(self, account_name, int_rate=0.02, balance=0):
        # """Adds a new bank account with the given name."""
        if account_name in self.accounts:
            print(f"Account '{account_name}' already exists.")
        else:
            self.accounts[account_name] = BankAccount(int_rate, balance)
            print(f"Account '{account_name}' added successfully.")
        return self

    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].balance += amount
        else:
            print(f"Account '{account_name}' does not exist.")
        return self

    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            account = self.accounts[account_name]
            if BankAccount.can_withdraw(account.balance, amount):
                account.balance -= amount
            else:
                print("Insufficient Funds")
        else:
            print(f"Account '{account_name}' does not exist.")
        return self

    def display_user_balance(self, account_name=None):
        # """Displays the balance of a specific account or all accounts."""
        if account_name:
            if account_name in self.accounts:
                account = self.accounts[account_name]
                print(f"User: {self.name}, Account: {account_name}, Balance: {account.balance}")
            else:
                print(f"Account '{account_name}' does not exist.")
        else:
            print(f"User: {self.name}, All Account Balances:")
            for acc_name, account in self.accounts.items():
                print(f"  Account: {acc_name}, Balance: {account.balance}")
        return self


# Create a user
user1 = User("Sabrina", "sab.harvey@gmail.com")

# Add multiple accounts
user1.add_account("Savings", int_rate=0.02, balance=500)
user1.add_account("Checking", int_rate=0.01, balance=1000)

# Perform transactions
user1.make_deposit("Savings", 300).make_deposit("Checking", 200)
user1.make_withdrawal("Savings", 100).make_withdrawal("Checking", 500)

# Display balances
user1.display_user_balance("Savings")
user1.display_user_balance("Checking")
user1.display_user_balance()

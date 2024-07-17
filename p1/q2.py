class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account {self.account_number} Balance: {self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, initial_balance)
            print(f"Account {account_number} created with balance {initial_balance}.")
        else:
            print(f"Account {account_number} already exists.")

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} closed.")
        else:
            print(f"Account {account_number} does not exist.")

    def display_accounts(self):
        if self.accounts:
            print(f"Bank {self.name} Accounts:")
            for account_number, account in self.accounts.items():
                account.display_balance()
        else:
            print("No accounts in the bank.")

# Instantiate and use the Bank and BankAccount classes
my_bank = Bank("MyBank")

# Create bank accounts
my_bank.create_account(1001, 500)
my_bank.create_account(1002, 1000)

# Display all bank accounts
my_bank.display_accounts()

# Deposit and withdraw from accounts
my_bank.accounts[1001].deposit(200)
my_bank.accounts[1001].display_balance()

my_bank.accounts[1002].withdraw(300)
my_bank.accounts[1002].display_balance()

# Close a bank account
my_bank.close_account(1001)
my_bank.display_accounts()

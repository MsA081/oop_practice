class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Balance: {self.balance}")


class Bank:
    balance = 0

    def __init__(self, name, *accounts):
        self.name = name
        self.accounts = list(accounts)

    def create_account(self, account_number):
        if account_number not in self.accounts:
            self.accounts.append(account_number)

    def close_account(self, account_number):
        if account_number in self.accounts:
            self.accounts.remove(account_number)

    @staticmethod
    def update_balance(amount):
        Bank.balance += amount

    def display_accounts(self):
        print(f"Bank Accounts : {self.accounts}")

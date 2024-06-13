import random


class BankAccount:
    Account_Numbers = set()

    def __init__(self, name0):
        for i in range(10_000_001):
            if (A_N := random.randrange(0, 10_000_000)) not in self.Account_Numbers:
                self.Account_Number = A_N
                self.Account_Numbers.add(self.Account_Number)
                break
        self.name = name0
        self.balance = 0

    def display(self):
        return f"hi {self.name}\nyour current balance {self.balance}"

    def deposit(self, name1, destination):
        if name1 in self.Account_Numbers:
            self.balance += destination
        else:
            print(f"Sorry, {name} does not exist")

    def withdraw(self, name2, amount):
        if name2 in self.Account_Numbers:
            if amount < self.balance:
                self.balance -= amount
            else:
                print("you cannot withdraw less than your balance")
        else:
            print(f"Sorry, {name} does not exist")


if __name__ == "__main__":
    while True:
        inp = input("Enter your choice : ")
        print(f"""
            {'=' * 20}Banner{'=' * 20}
            \t 1 : Register
            \t 2 : Deposit
            \t 3 : Withdraw
            \t 4 : Exit
            {'=' * 20}======{'=' * 20}
            """)
        if int(inp) == 1:
            name = input("What is your name? ")
            account = BankAccount(name)
            account.display()
        elif int(inp) == 2:
            name = input("What is your name? ")
            deposit = input("How much money would you like to deposit? ")
            account = BankAccount(name)
            account.deposit(name, deposit)
        elif int(inp) == 3:
            name = input("What is your name? ")
            withdraw = input("How much money would you like to withdraw? ")
            account = BankAccount(name)
            account.withdraw(name, withdraw)
        else:
            exit()


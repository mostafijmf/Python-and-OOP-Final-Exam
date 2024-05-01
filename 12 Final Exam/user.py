from abc import ABC
from random import randint
from datetime import datetime
from bank import Bank

bank = Bank()

class User(ABC):
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address


class AccountHolder(User):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_number = randint(10000, 999999)
        self.account_type = account_type
        self.balance = 0
        self.transaction = []
        self.loan = []
        bank.users.append(self)

    def deposit(self, amount):
        self.balance += amount
        summary = {
            'transaction': 'Deposit',
            'amount': amount,
            'time': datetime.now()
        }
        self.transaction.append(summary)
        bank.user_deposit(self, amount)
        print(f"You have deposited successfully!. Your current balance: {self.balance}")

    def withdraw(self, amount):
        if bank.total_balance < amount:
            print("Sorry! The bank is bankrupt.")
        elif amount > self.balance:
            print(f"Withdrawal amount exceeded. Your current balance: {self.balance}")
        else:
            self.balance -= amount
            summary = {
                'transaction': 'Withdraw',
                'amount': amount,
                'time': datetime.now()
            }
            self.transaction.append(summary)
            bank.user_withdraw(self, amount)
            print(f"Withdraw successful!. Your current balance: {self.balance}")

    def check_balance(self):
        print(f"Your current balance: {self.balance}")

    def check_transaction(self):
        if len(self.transaction) > 0:
            for item in self.transaction:
                print(f"Transaction type: {item['transaction']}, Amount: {item['amount']}, Date: {item['time']}")
        else:
            print("Transaction history is empty!")

    def take_loan(self, amount):
        if bank.is_loan_active == False:
            print("Loan feature is off!")
        elif bank.total_balance < amount:
            print("Your loan amount is more than the bank balance.")
        elif len(self.loan) < 2:
            self.loan.append(amount)
            self.balance += amount
            summary = {
                'transaction': 'Loan',
                'amount': amount,
                'time': datetime.now()
            }
            self.transaction.append(summary)
            bank.user_loan(self, amount)
            print("Congratulation! You got a loan successfully")
        else:
            print(f"Sorry! You can not take the loan more than 2")

    def find_user_by_acc(self, acc):
        for user in bank.users:
            if user.account_number == acc:
                return user

    def transfer(self, account_number, amount):
        user = self.find_user_by_acc(account_number)

        if amount > self.balance:
            print("Insufficient balance!")
        elif user:
            self.balance -= amount
            summary = {
                'transaction': f'Transfer to {account_number}',
                'amount': amount,
                'time': datetime.now()
            }
            self.transaction.append(summary)
            bank.user_transfer(self, account_number, amount)
            print(f"You have send {amount} to account-{account_number} successfully")
        else:
            print("Account does not exist")


class Admin(User):
    def __init__(self, name, email, address, password) -> None:
        super().__init__(name, email, address)
        self.password = password

    def find_user(self, email):
        for user in bank.users:
            if user.email.lower() == email.lower():
                return user

    def delete_user(self, email):
        user = self.find_user(email)
        bank.users.remove(user)
        print("User deleted successfully")

    def show_users(self):
        if len(bank.users) > 0:
            for user in bank.users:
                print(f"Account Number: {user.account_number}, Name: {user.name}, Email: {user.email}, Address: {user.address}, Account Type: {user.account_type}")
        else:
            print("No users account")

    def check_bank_balance(self):
        print(bank.total_balance)

    def check_total_loan(self):
        total_loan = 0
        for user in bank.users:
            total_loan += len(user.loan)
        print(f"{total_loan}")

    def loan_feature(self):
        if bank.is_loan_active:
            bank.is_loan_active = False
            print("Loan feature is off")

        else:
            bank.is_loan_active = True
            print("Loan feature is on")

from abc import ABC
from datetime import datetime


class Bank(ABC):
    def __init__(self):
        self.name = 'IBBL'
        self.users = []
        self.total_balance = 100000
        self.is_loan_active = True

    def user_deposit(self, user, amount):
        for index, u in enumerate(self.users):
            if u.account_number == user.account_number:
                self.users[index] = user
                self.total_balance += amount
                break

    def user_withdraw(self, user, amount):
        for index, u in enumerate(self.users):
            if u.account_number == user.account_number:
                self.users[index] = user
                self.total_balance -= amount
                break

    def user_loan(self, user, loan):
        for index, u in enumerate(self.users):
            if u.account_number == user.account_number:
                self.users[index] = user
                # self.total_balance -= loan
                break

    def user_transfer(self, from_user, to_user, amount):
        for index, u in enumerate(self.users):
            if u.account_number == to_user:
                self.users[index].balance += amount
                summary = {
                    'transaction': f'Transfer from {from_user.account_number}',
                    'amount': amount,
                    'time': datetime.now()
                }
                self.users[index].transaction.append(summary)
                
            if u.account_number == from_user.account_number:
                self.users[index] = from_user

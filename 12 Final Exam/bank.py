from abc import ABC
from random import randint
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
        print(f"You have deposited successfully!. Your current balance: {
              self.balance}")

    def withdraw(self, amount):
        if bank.total_balance < amount:
            print("Sorry! The bank is bankrupt.")
        elif amount > self.balance:
            print(f"Withdrawal amount exceeded. Your current balance: {
                  self.balance}")
        else:
            self.balance -= amount
            summary = {
                'transaction': 'Withdraw',
                'amount': amount,
                'time': datetime.now()
            }
            self.transaction.append(summary)
            bank.user_withdraw(self, amount)
            print(f"Withdraw successful!. Your current balance: {
                  self.balance}")

    def check_balance(self):
        print(f"Your current balance: {self.balance}")

    def check_transaction(self):
        if len(self.transaction) > 0:
            for item in self.transaction:
                print(f"Transaction type: {item['transaction']}, Amount: {
                      item['amount']}, Date: {item['time']}")
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
            print(f"You have send {
                  amount} to account-{account_number} successfully")
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
                print(f"Account Number: {user.account_number}, Name: {user.name}, Email: {
                      user.email}, Address: {user.address}, Account Type: {user.account_type}")
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




# ********** replica system ******************
def admin():
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    address = input('Enter Address: ')
    password = int(input('Enter Number Password: '))
    ad = Admin(name, email, address, password)
    while True:
        print(f"************ Welcome {ad.name}! ************")
        print("1. Delete a user account")
        print("2. Show all users")
        print("3. Check the Bank balance")
        print("4. Check the total loan")
        print("5. On or Off the loan feature")
        print("6. Exit")
        opt = input('Enter Option: ')
        if opt == '6':
            break
        elif opt == '1':
            email = input('Enter user email: ')
            ad.delete_user(email)
        elif opt == '2':
            ad.show_users()
        elif opt == '3':
            ad.check_bank_balance()
        elif opt == '4':
            ad.check_total_loan()
        elif opt == '5':
            ad.loan_feature()
        else:
            print("Invalid option!")


def user():
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    address = input('Enter Address: ')
    print("****** Choose user account type ******")
    print("1. Savings")
    print("2. Current")
    acc_opt = int(input("Enter option: "))
    account_type = ['savings', 'current']
    user = AccountHolder(name, email, address, account_type[acc_opt-1])
    while True:
        print(f"************ Welcome {user.name}! ************")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction history")
        print("5. Take a loan")
        print("6. Transfer balance")
        print("7. Exit")
        opt = input('Enter Option: ')
        if opt == '7':
            break
        elif opt == '1':
            user.check_balance()
        elif opt == '2':
            amount = int(input(f"Enter Amount: "))
            user.deposit(amount)
        elif opt == '3':
            amount = int(input(f"Enter Amount: "))
            user.withdraw(amount)
        elif opt == '4':
            user.check_transaction()
        elif opt == '5':
            amount = int(input(f"Enter Amount: "))
            user.take_loan(amount)
        elif opt == '6':
            account_number = int(input(f"Enter Account Number: "))
            amount = int(input(f"Enter Amount: "))
            user.transfer(account_number, amount)
        else:
            print("Invalid option!")


while True:
    print("************ Welcome! ************")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    opt = input('Enter Option: ')
    if opt == '3':
        break
    elif opt == '1':
        admin()
    elif opt == '2':
        user()
    else:
        print("Invalid option!")

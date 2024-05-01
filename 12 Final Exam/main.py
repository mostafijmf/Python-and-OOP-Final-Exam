from user import AccountHolder, Admin

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

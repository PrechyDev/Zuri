from datetime import datetime
now = datetime.now()
date_time = now.strftime("%H:%M:%S %d/%m/%Y")

username = input("Enter your username: \n")
allowed_users = ['Prechy', 'Uche', 'Praise']
allowed_passwords = ['prechy', 'uche', 'praise']
balance = {'Prechy': 10000, 'Uche': 20000, 'Praise': 50000}

if username in allowed_users:
    user_id = allowed_users.index(username)
    password = input("Enter your password: \n")

    if password == allowed_passwords[user_id]:
        print("Welcome %s \n" %username)

        print('Current date and time \n %s \n' %date_time)

        # options
        print('What would you like to do?')
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Complaint')

        selected_option = int(input('\nPlease select an option: \n'))

        if selected_option == 1:
            withdrawn = int(input('How much would you like to withdraw? \n'))
            balance[username] -= withdrawn
            print('Take your cash')
        
        elif selected_option == 2:
            deposit = int(input('How much would you like to deposit? \n'))
            current_balance = balance[username] + deposit
            print('Your current account balance is %s' %current_balance)

        elif selected_option == 3:
            complaint = input('What would you like to report? \n')

        else:
            print('Invalid option selected, try again')

    else:
        print("Incorrect password, please try again")

else:
    print("Name not found, please ty again")
    



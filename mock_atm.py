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

        while selected_option:
            if selected_option == 1:
                withdrawn = int(input('How much would you like to withdraw? \n'))
                if withdrawn >= balance[username]:
                    
                    # User forgotten amount left in wallet
                    alert = input ('Insufficient Funds! \n Would you like to give it another try?Y/n: ')
                    if alert == 'Y':
                        selected_option
                        
                     # Outro message for ending transaction   
                    else: print('Thanks For Banking With Us.')
                     # end transaction
                    quit()
                else:
                    balance[username] -= withdrawn
                    print('Take your cash')
                    quit()
                    
                    
         elif selected_option == 2:
            deposit = int(input('How much would you like to deposit? \n'))
            current_balance = balance[username] + deposit
            
            #confirmation of transaction 
            print(f' {deposit} has been successfully deposited!! Your current account balance is {current_balance}')
            quit()

        elif selected_option == 3:
            complaint = input('What would you like to report? \n')

        else:
            print('Invalid option selected, try again')

    else:
        print("Incorrect password, please try again")

else:
    print("Name not found, please ty again")
    



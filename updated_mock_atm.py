import random

database = {}

#initializating the system
def init():
    print('Welcome to Bank P')
    
    have_account = int(input('Do you have an account with us? \n 1 (yes) 2 (no) \n'))

    if(have_account == 1):
        login()
    elif(have_account == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()


#login
# - enter acct_number and password
def login():
    print('***Login to your account***')

    user_acct = int(input('Enter your account number \n'))
    user_pwd = input('Enter your password \n')

    for acct_no, user_details in database.items():
        if user_acct == acct_no:
            if user_pwd == user_details[3]:
                print('Welcome %s %s' %(user_details[0], user_details[1]))
                bank_operations(user_details)
        else: 
            print('Invalid account or password, try again')
            login()

    


#register
# - create email, f_name, l_name, password
# - generate user_account
def register():
    print('********Register******')
    email = input('Enter your email address: \n')
    f_name = input('Enter your first name: \n')
    l_name = input('Enter your last name: \n')
    password = input('Create a strong password: \n') 

    account_number = generate_acct_number()
    balance = 0

    database[account_number] = [f_name, l_name, email, password, balance]
    
    print('Welcome %s, your account has been created \n' %f_name)
    print('Your account number is %s \n' %account_number)
    print('Ensure your keep your account number and password safe')
    login()


#bank operations
def bank_operations(user):
    print('What would you like to do? \n')
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Check account balance')
    print('4. Logout')
    print('5. Exit')

    selected_option = int(input('Select an option \n'))

    if(selected_option == 1):
        deposit(user) 
    elif(selected_option == 2):
        withdraw(user)
    elif(selected_option == 3):
        check_balance(user)
    elif(selected_option == 4):
        logout()
    elif(selected_option == 5):
        exit()
    else:
        print('Invalid option, try again')
        bank_operations(user)


def withdraw(user):
    amount = int(input('How much would you like to withdraw? \n'))
    user[-1] -= amount #subtracts amount from user_balance
    print('Take your cash')
    print('Do you want to make another transaction?')
    option = int(input(' 1.Yes 2.No \n'))

    if(option == 1):
        bank_operations(user)
    elif(option == 2):
        print('Thank you for banking with us')
        exit()

def deposit(user):
    amount = int(input('How much do you want to deposit? \n'))
    user[-1] += amount #subtracts amount from user_balance
    acct_balance = user[-1]
    print('Deposit successful')
    print('Your current account balance is %s' %acct_balance)
    print('Do you want to make another transaction?')
    option = int(input(' 1.Yes 2.No \n'))

    if(option == 1):
        bank_operations(user)
    else:
        print('Thank you for banking with us')
        exit()

def check_balance(user):
    acct_balance = user[-1]
    print('Your account balance is %s' %acct_balance)

    print('Do you want to make another transaction?')
    option = int(input(' 1.Yes 2.No \n'))

    if(option == 1):
        bank_operations(user)
    else:
        print('Thank you for banking with us')
        exit()


def logout():
    login()


## generating account number for new user
def generate_acct_number():
    return random.randrange(1111111111,9999999999)


### ACTUAL BANKING SYSTEM ### 
init()

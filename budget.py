class Budget:
    '''
    The Budget class creates budget instances for various categories.
    A user can add funds, withdraw funds  and calculate the balance in each  category
    A user can also transfer funds between categories.
    '''
    ##total balance for all categories
    total_balance = 0
    def net_balance():
        print(f'The net balance of your budget categories is {Budget.total_balance}')

    def __init__(self, category):
        self.name = category
        self.balance = 0

    def deposit(self):
        amount = int(input(f'How much do you want to deposit for {self.name}\n'))
        self.balance += amount
        Budget.total_balance += amount
        print(f'Your current budget for {self.name} is {self.balance} ')

    def withdraw(self):
        amount = int(input(f'How much do you want to withdraw from your {self.name} account?\n'))
        self.balance -= amount
        Budget.total_balance -= amount

        print(f'You just withdrew {amount}, you have {self.balance} left in your {self.name} account')
    
    def transfer(self, other):
        amount = int(input(f'How much do you want to transfer to your {other.name} account?\n'))
        self.balance -= amount
        other.balance += amount

        print('Transfer successful!')
        print(f'You have left in {self.balance} in your {self.name} account and {other.balance} in your {other.name} account')
        

    def check_balance(self):
        print(f'You have {self.balance} remaining in your {self.name} account')

   

## categories
#food = Budget('Food')
#transport = Budget('Transportation')
#clothing = Budget('Clothing')
#entertain = Budget('Entertainment')
#bills = Budget('Bills')
#rent = Budget('Rent')
#other = Budget('Others')

##tests
#food.deposit()
#food.withdraw()
#food.check_balance()
#bills.deposit()
#Budget.net_balance()
#food.transfer(rent)

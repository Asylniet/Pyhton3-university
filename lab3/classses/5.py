class Account:    
    def __init__(self, owner, balance) :
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'
    
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} Deposit added\nYour balance - {self.balance}')
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount} Withdrawl taken \nYour balance - {self.balance}')
        else :
            print(f'Not enough money!\nYou need {amount - self.balance} more money on your balance')
        
person = Account('Aman', 100)
person.deposit(500)
person.withdraw(50)
person.withdraw(1000)
